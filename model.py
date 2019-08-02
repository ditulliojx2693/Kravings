from google.appengine.ext import ndb

class UserData(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    loggedin = ndb.BooleanProperty()

class OldResults(ndb.Model):
    img = ndb.StringProperty()
    login_info = ndb.StringProperty()
