from google.appengine.ext import ndb

class Message(ndb.Model):
    sender = ndb.StringProperty()
    recipient = ndb.StringProperty()
    subject = ndb.StringProperty()
    message = ndb.StringProperty()
    sent = ndb.DateTimeProperty(auto_now_add=True)