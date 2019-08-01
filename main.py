import webapp2
import jinja2
import os
import requests
import requests_toolbelt.adapters.appengine
import json
import random
from google.appengine.ext import vendor
from google.appengine.api import urlfetch
from flask import Flask, redirect, url_for, render_template, request
from google.appengine.api import users
from google.appengine.ext import ndb
from model import UserData


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class CssiUser(ndb.Model):
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()

class LoginPage(webapp2.RequestHandler):
    def post(self):
        login_template = the_jinja_env.get_template('templates/login2.html')
        if self.request.get('first_name') != "":
            first_name = self.request.get('first_name')
            last_name = self.request.get('last_name')
            username = self.request.get('username')
            password = self.request.get('password')
            secure_data = UserData(first_name = first_name, last_name = last_name, username = username, password = password, loggedin = False)
            secure_data.put()
        self.response.write(login_template.render())
    def get(self):
        login_template = the_jinja_env.get_template('templates/login2.html')
        self.response.write(login_template.render())

class HomePage(webapp2.RequestHandler):
    def post(self):
        home_template = the_jinja_env.get_template('templates/home.html')
        redirect_template = the_jinja_env.get_template('templates/redirect.html')
        username_attempt = self.request.get('usernameAttempt')
        password_attempt = self.request.get('passwordAttempt')
        check_cred = UserData.query().filter(UserData.username == username_attempt, UserData.password == password_attempt).fetch()
        if len(check_cred) == 0:
            self.response.write(redirect_template.render())
        else:
            user = check_cred[0].key.get()
            userInfo = check_cred[0]
            print(self.request.cookies.get("loggedin"))
            user.loggedin = True
            user.put()
            self.response.set_cookie("loggedin", userInfo.username)
            self.response.set_cookie("firstname", userInfo.first_name)
            self.response.set_cookie("lastname", userInfo.last_name)
            user_dict = {
                "firstname": userInfo.first_name,
                "lastname": userInfo.last_name,
            }
            print(user_dict)
            self.response.write(home_template.render(user_dict))
    def get(self):
        home_template = the_jinja_env.get_template('templates/home.html')
        user_dict = {
            "firstname": self.request.cookies.get("firstname"),
            "lastname": self.request.cookies.get("lastname"),
        }
        self.response.write(home_template.render(user_dict))

class SignInPage(webapp2.RequestHandler):
    def post(self):
        signin_template = the_jinja_env.get_template('templates/signin.html')
        self.response.write(signin_template.render())

class QuizPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        quiz_template = the_jinja_env.get_template('templates/quiz.html')
        redirect_template = the_jinja_env.get_template('templates/redirect.html')
        if self.request.cookies.get("loggedin"):
            questions_dict = {
                "q1": "Do you want something savory?",
                "q2": "Do you want something sweet?",
                "q3": "Would you like something vegan or vegitarian?",
                "q4": "Are you looking for spicy food?",
                "q5": "Would you like something rich?",
                "q6": "Do you want something you can take to go?",
                "q7": "Would you like something unhealthy?",
                "q8": "Do you want to eat something healthy and light?",
                "q9": "Would you like to try food that uses many different kinds of seasonings?",
                "q10": "Are you a fan of seafood?",
                "firstname": self.request.cookies.get("firstname"),
                "lastname": self.request.cookies.get("lastname"),
            }
            self.response.write(quiz_template.render(questions_dict))  # the response
        else:
            self.response.write(redirect_template.render())

class ResultsPage(webapp2.RequestHandler):
    def get(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        img = ""
        fooditem = ""
        ran_num = random.randint(1,16)
        print(ran_num)
        if ran_num == 1:
            img = "images/burger.png"
            fooditem = "Burger"
        elif ran_num == 2:
            img = "images/chinese.png"
            fooditem = "Chinese Food"
        elif ran_num == 3:
            img = "images/taco.png"
            fooditem = "Taco"
        elif ran_num == 4:
            img = "images/boba.png"
            fooditem = "Boba"
        elif ran_num == 5:
            img = "images/veggie.png"
            fooditem = "Veggie Burger"
        elif ran_num == 6:
            img = "images/fries.png"
            fooditem = "Fries"
        elif ran_num == 7:
            img = "images/crab.png"
            fooditem = "Seafood"
        elif ran_num == 8:
            img = "images/indian.png"
            fooditem = "Indian Food"
        elif ran_num == 9:
            img = "images/tofu.png"
            fooditem = "Tofu"
        elif ran_num == 10:
            img = "images/ice_cream.png"
            fooditem = "Ice Cream"
        elif ran_num == 11:
            img = "images/churros.png"
            fooditem = "Churros"
        elif ran_num == 12:
            img = "images/sushi.png"
            fooditem = "Sushi"
        elif ran_num == 13:
            img = "images/acai.png"
            fooditem = "Acai Bowl"
        elif ran_num == 14:
            img = "images/soup.png"
            fooditem = "Soup"
        elif ran_num == 15:
            img = "images/poke.png"
            fooditem = "Poke"
        else:
            img = "images/nuggets.png"
            fooditem = "Chicken Nuggets"
        food_display_dict = {
            "img": img,
            "fooditem": fooditem
        }
        self.response.write(results_template.render(food_display_dict))
    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        burger_count = int(self.request.get("burger1")) + int(self.request.get("burger2"))
        dessert_count = int(self.request.get("ice_cream1")) + int(self.request.get("ice_cream2"))
        tofu_count = int(self.request.get("tofu1")) + int(self.request.get("tofu2"))
        indian_count = int(self.request.get("beef1")) + int(self.request.get("beef2"))
        seafood_count = int(self.request.get("seafood1")) + int(self.request.get("seafood2"))
        global fooditem
        fooditem = ""
        img = ""
        if burger_count > dessert_count and burger_count > tofu_count and burger_count > indian_count and burger_count > seafood_count:
            img = "images/burger.png"
            fooditem = "A Burger"
        elif dessert_count > burger_count and dessert_count > tofu_count and dessert_count > indian_count and dessert_count > seafood_count:
            img = "images/ice_cream.png"
            fooditem = "Ice Cream"
        elif tofu_count > burger_count and tofu_count > dessert_count and tofu_count > indian_count and tofu_count > seafood_count:
            img = "images/salad.png"
            fooditem = "Salad"
        elif indian_count > burger_count and indian_count > dessert_count and indian_count > tofu_count and indian_count > seafood_count:
            img = "images/indian.png"
            fooditem = "Indian Food"
        elif seafood_count > burger_count and seafood_count > dessert_count and seafood_count > tofu_count and seafood_count > indian_count:
            img ="images/crab.png"
            fooditem = "Seafood"
        elif burger_count == dessert_count and burger_count > indian_count and burger_count > seafood_count and burger_count > tofu_count:
            img = "images/fries.png"
            fooditem = "Fries"
        elif burger_count == tofu_count and burger_count > dessert_count and burger_count > indian_count  and burger_count > seafood_count:
            img = "images/veggie.png"
            fooditem = "Veggie Burger"
        elif burger_count == indian_count and burger_count > tofu_count and burger_count > dessert_count and burger_count > seafood_count:
            img = "images/chinese.png"
            fooditem = "Chinese Food"
        elif burger_count == seafood_count and burger_count > tofu_count and burger_count > indian_count and burger_count > dessert_count:
            img = "images/taco.png"
            fooditem = "Fish Tacos"
        elif  dessert_count == tofu_count:
            img = "images/boba.png"
<<<<<<< HEAD
            fooditem= "Boba"
=======
            fooditem = "Boba"
>>>>>>> 12340c7d8c991225b1e3bf2cd547d7faf2aee0f0
        elif dessert_count == indian_count and dessert_count > tofu_count and dessert_count > seafood_count and dessert_count > burger_count:
            img = "images/churros.png"
            fooditem = "Churros"
        elif dessert_count == seafood_count:
            img = "images/sushi.png"
            fooditem = "Sushi"
        elif tofu_count == indian_count and tofu_count > seafood_count and tofu_count > dessert_count and tofu_count > burger_count:
            img = "images/acai.png"
            fooditem = "Acai Bowl"
        elif tofu_count == seafood_count and tofu_count > indian_count and tofu_count > dessert_count and tofu_count > burger_count:
            img = "images/soup.png"
            fooditem= "Soup"
        elif indian_count == seafood_count and indian_count > tofu_count and indian_count > dessert_count and indian_count > burger_count:
            img = "images/poke.png"
            fooditem = "Poke"
        else:
            img = "images/nuggets.png"
            fooditem = "Chicken Nuggets"
        food_display_dict = {
            "img": img,
            "fooditem": fooditem,
            "firstname": self.request.cookies.get("firstname"),
            "lastname": self.request.cookies.get("lastname"),
        }
        self.response.write(results_template.render(food_display_dict))   # the response

class AboutUsPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        aboutUs_template = the_jinja_env.get_template('templates/AboutUs.html')
        user_dict = {
            "firstname": self.request.cookies.get("firstname"),
            "lastname": self.request.cookies.get("lastname"),
        }
        self.response.write(aboutUs_template.render(user_dict))  # the response
        #self.response.write("about us working")
class RedirectPage(webapp2.RequestHandler):
    def get(self):
        redirect_template = the_jinja_env.get_template('templates/redirect.html')
        self.response.delete_cookie("loggedin")
        self.response.delete_cookie("firstname")
        self.response.delete_cookie("lastname")
        self.response.write(redirect_template.render())

class YelpPage(webapp2.RequestHandler):
    def get(self):
        ClientId = 'Gt46dGLdwKMdznkcqbizJQ'
        api_key = 'eJCV1UT9rP5M8_I8QrS2KmdyC7D3dnBWL8B9KxkwhZJgypDE9cafXOvTvz-eLXz5ghkAJ2pllHIT_0P1ye2NueygCLZmmyz4cQ2XQMnc7lu-piHWLcBytmRi8m1AXXYx'
        endpoint = 'https://api.yelp.com/v3/businesses/search'
        headers = {'Authorization': 'Bearer %s' % api_key}
        params = {'term':fooditem,'limit':10,'radius':10000,'location':'Seattle'}
        requests_toolbelt.adapters.appengine.monkeypatch()
        req=requests.get(url=endpoint, params=params, headers=headers)
        business_data = req.json()
        print(business_data.keys())
        for biz in business_data['businesses']:
            print (biz['name'])
        yelp_dict = {
            'businesses': business_data,
            "firstname": self.request.cookies.get("firstname"),
            "lastname": self.request.cookies.get("lastname"),
        }
        yelppage_template = the_jinja_env.get_template('templates/YelpPage.html')
        self.response.write(yelppage_template.render(yelp_dict))
# the app configuration section
app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/home', HomePage),
    ('/signup', SignInPage),
    ('/quiz', QuizPage),
    ('/results', ResultsPage),
    ('/yelppage', YelpPage),
    ('/aboutus', AboutUsPage),
    ('/logout', RedirectPage),
], debug=True)
