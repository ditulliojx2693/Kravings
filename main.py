import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):  # for a get request
        home_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(home_template.render())  # the response

class QuizPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        quiz_template = the_jinja_env.get_template('templates/quiz.html')
        questions_dict = {
            "q1": "Do you want a burger?",
            "q2": "Do you want ice cream?",
            "q3": "Do you want tofu?",
            "q4": "Are you looking for beef?",
            "q5": "Do you want seafood?",
        }
        self.response.write(quiz_template.render(questions_dict))  # the response
class ResultsPage(webapp2.RequestHandler):
    def post(self):  # for a get request
        results_template = the_jinja_env.get_template('templates/results.html')
        burger_count = int(self.request.get("burger1"))
        dessert_count = int(self.request.get("ice_cream1"))
        tofu_count = int(self.request.get("tofu1"))
        beef_count = int(self.request.get("beef1"))
        seafood_count = int(self.request.get("seafood1"))
        fooditem = ""
        img = ""
        if burger_count > dessert_count and burger_count > tofu_count and burger_count > beef_count and burger_count > seafood_count:
            img = "images/burger.png"
            fooditem = "A Burger"
        elif dessert_count > burger_count and dessert_count > tofu_count and dessert_count > beef_count and dessert_count > seafood_count:
            img = "images/ice_cream.png"
            fooditem = "Ice Cream"
        elif tofu_count > burger_count and tofu_count > dessert_count and tofu_count > beef_count and tofu_count > seafood_count:
            img = "images/tofu.png"
            fooditem = "Tofu"
        elif beef_count > burger_count and beef_count > dessert_count and beef_count > tofu_count and beef_count > seafood_count:
            img = "images/beef.jpg"
            fooditem = "Beef"
        elif seafood_count > burger_count and seafood_count > dessert_count and seafood_count > tofu_count and seafood_count > beef_count:
            img ="https://media.istockphoto.com/vectors/sea-crab-icon-vector-id869408302?k=6&m=869408302&s=612x612&w=0&h=wcBuLlH_oe7gAzb5XF_uPWxzBY88KRAAiwzsj-76yWs="
            fooditem = "Seafood"
        food_display_dict = {
            "img": img,
            "fooditem": fooditem
        }
        self.response.write(results_template.render(food_display_dict))  # the response

class AboutUsPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        aboutUs_template = the_jinja_env.get_template('templates/AboutUs.html')
        self.response.write(aboutUs_template.render())  # the response
        #self.response.write("about us working")


# the app configuration section
app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/quiz', QuizPage),
    ('/results', ResultsPage),
    ('/aboutus', AboutUsPage),
], debug=True)
