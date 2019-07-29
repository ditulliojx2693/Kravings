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
        self.response.write("homepage working")

class QuizPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        quiz_template = the_jinja_env.get_template('templates/quiz.html')
        questions_dict = {
            "q1": "Do you want a burger?",
            "q2": "Do you want ice cream?",
            "q3": "Do you want tofu?",
            "q4": "Are you looking beef?",
            "q5": "Do you want seafood?",
        }

        self.response.write(quiz_template.render(questions_dict))  # the response
        self.response.write("quiz working")

class ResultsPage(webapp2.RequestHandler):
    def get(self):  # for a get request
        results_template = the_jinja_env.get_template('templates/results.html')
        self.response.write(results_template.render())  # the response
        self.response.write("results working")

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
