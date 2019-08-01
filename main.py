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

class HomePage(webapp2.RequestHandler):
    def post(self):  # for a get request
        home_template = the_jinja_env.get_template('templates/home.html')
        username_attempt = self.request.get('usernameAttempt')
        password_attempt = self.request.get('passwordAttempt')
        check_cred = UserData.query().filter(UserData.username == username_attempt, UserData.username == password_attempt).fetch()
        if check_cred == []:
            print('Your username or password is incorrect!')
        else:
            login == True;
        self.response.write(home_template.render())  # the response
    def get(self):
        home_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(home_template.render())

class LoginPage(webapp2.RequestHandler):
    def get(self):
        login_template = the_jinja_env.get_template('templates/login2.html')
        self.response.write(login_template.render())
    def post(self):
        login_template = the_jinja_env.get_template('templates/login2.html')
        first_name = self.request.get('first_name')
        last_name = self.request.get('last_name')
        username = self.request.get('username')
        password = self.request.get('password')
        secure_data = UserData(first_name = first_name, last_name = last_name, username = username, password = password)
        secure_data.put()
        self.response.write(login_template.render())

class SignInPage(webapp2.RequestHandler):
    def post(self):
        signin_template = the_jinja_env.get_template('templates/signin.html')
        self.response.write(signin_template.render())

class SignUpPage(webapp2.RequestHandler):
    def get(self):
        signup_template = the_jinja_env.get_template('templates/signup.html')
        self.response.write(signup_template.render())
    def get(self):
      user = users.get_current_user()
      # If the user is logged in...
      if user:
        email_address = user.nickname()
        cssi_user = CssiUser.get_by_id(user.user_id())
        signout_link_html = '<a href="%s">sign out</a>' % (
            users.create_logout_url('/'))
        # If the user has previously been to our site, we greet them!
        if cssi_user:
          self.response.write('''
              Welcome %s %s (%s)! <br> %s <br>''' % (
                cssi_user.first_name,
                cssi_user.last_name,
                email_address,
                signout_link_html))
        # If the user hasn't been to our site, we ask them to sign up
        else:
          self.response.write('''
              Welcome to our site, %s!  Please sign up! <br>
              <form method="post" action="/">
              <input type="text" name="first_name">
              <input type="text" name="last_name">
              <input type="submit">
              </form><br> %s <br>
              ''' % (email_address, signout_link_html))
      # Otherwise, the user isn't logged in!
      else:
        self.response.write('''
          Please log in to use our site! <br>
          <a href="%s">Sign in</a>''' % (
            users.create_login_url('/home')))

    def post(self):
      user = users.get_current_user()
      if not user:
        # You shouldn't be able to get here without being logged in
        self.error(500)
        return
      cssi_user = CssiUser(
          first_name=self.request.get('first_name'),
          last_name=self.request.get('last_name'),
          id=user.user_id())
      cssi_user.put()
      self.response.write('Thanks for signing up, %s!' %
          cssi_user.first_name)

class QuizPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        quiz_template = the_jinja_env.get_template('templates/quiz.html')
        questions_dict = {
            "q1": "Do you want something savory?",
            "q2": "Do you want something sweet?",
            "q3": "Are you interested in trying something healthy?",
            "q4": "Are you looking for spicy food?",
            "q5": "Would you like an alternative to meat?",
            "q6": "Do you like fast food?",
            "q7": "Would you like to customize your food?",
            "q8": "Do you want to eat food that makes you feel good about yourself?",
            "q9": "Would you like to try food that uses many different kinds of seasonings?",
            "q10": "Are you a fan of things like sushi?",
        }
        self.response.write(quiz_template.render(questions_dict))  # the response

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
            img = "https://media.istockphoto.com/vectors/sea-crab-icon-vector-id869408302?k=6&m=869408302&s=612x612&w=0&h=wcBuLlH_oe7gAzb5XF_uPWxzBY88KRAAiwzsj-76yWs="
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
        fooditem = ""
        img = ""
        if burger_count > dessert_count and burger_count > tofu_count and burger_count > indian_count and burger_count > seafood_count:
            img = "images/burger.png"
            fooditem = "A Burger"
        elif dessert_count > burger_count and dessert_count > tofu_count and dessert_count > indian_count and dessert_count > seafood_count:
            img = "images/ice_cream.png"
            fooditem = "Ice Cream"
        elif tofu_count > burger_count and tofu_count > dessert_count and tofu_count > indian_count and tofu_count > seafood_count:
            img = "images/tofu.png"
            fooditem = "Tofu"
        elif indian_count > burger_count and indian_count > dessert_count and indian_count > tofu_count and indian_count > seafood_count:
            img = "images/indian.png"
            fooditem = "Indian Food"
        elif seafood_count > burger_count and seafood_count > dessert_count and seafood_count > tofu_count and seafood_count > indian_count:
            img ="https://media.istockphoto.com/vectors/sea-crab-icon-vector-id869408302?k=6&m=869408302&s=612x612&w=0&h=wcBuLlH_oe7gAzb5XF_uPWxzBY88KRAAiwzsj-76yWs="
            fooditem = "Seafood"
        elif burger_count == dessert_count:
            img = "images/fries.png"
            fooditem = "Fries"
        elif burger_count == tofu_count:
            img = "images/veggie.png"
            fooditem = "Veggie Burger"
        elif burger_count == indian_count:
            img = "images/chinese.png"
            fooditem = "Chinese Food"
        elif burger_count == seafood_count:
            img = "images/taco.png"
            fooditem = "Fish Tacos"
        elif  dessert_count == tofu_count:
            img = "images/boba.png"
            fooditem= "Boba"
        elif dessert_count == indian_count:
            img = "images/churros.png"
            fooditem = "Churros"
        elif dessert_count == seafood_count:
            img = "images/sushi.png"
            fooditem = "Sushi"
        elif tofu_count == indian_count:
            img = "images/acai.png"
            fooditem = "Acai Bowl"
        elif tofu_count == seafood_count:
            img = "images/soup.png"
            fooditem= "Soup"
        elif indian_count == seafood_count:
            img = "images/poke.png"
            fooditem = "Poke"
        else:
            img = "images/nuggets.png"
            fooditem = "Chicken Nuggets"
        food_display_dict = {
            "img": img,
            "fooditem": fooditem
        }
        self.response.write(results_template.render(food_display_dict))   # the response

class AboutUsPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        aboutUs_template = the_jinja_env.get_template('templates/AboutUs.html')
        self.response.write(aboutUs_template.render())  # the response
        #self.response.write("about us working")

class YelpPage(webapp2.RequestHandler):
    def get(self):
        api_key = 'eJCV1UT9rP5M8_I8QrS2KmdyC7D3dnBWL8B9KxkwhZJgypDE9cafXOvTvz-eLXz5ghkAJ2pllHIT_0P1ye2NueygCLZmmyz4cQ2XQMnc7lu-piHWLcBytmRi8m1AXXYx'
        headers = {'Authorization': 'Bearer %s' % api_key}
        url='https://api.yelp.com/v3/businesses/search'
        params = {'term':'fooditem','location':'New York City'}
        requests_toolbelt.adapters.appengine.monkeypatch()
        req=requests.get(url, params=params, headers=headers)
        parsed = json.loads(req.text)
        businesses = parsed["businesses"]
        for business in businesses:
            print("Name:", business["name"])
            print("Rating:", business["rating"])
            print("Address:", " ".join(business["location"]["display_address"]))
            print("Phone:", business["phone"])
            print("\n")
        yelppage_template = the_jinja_env.get_template('templates/YelpPage.html')
        self.response.write(yelppage_template.render())
# the app configuration section
app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/home', HomePage),
    ('/signup', SignInPage),
    ('/quiz', QuizPage),
    ('/results', ResultsPage),
    ('/yelppage', YelpPage),
    ('/aboutus', AboutUsPage),
], debug=True)
