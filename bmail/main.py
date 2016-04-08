#!/usr/bin/env python
import os
import jinja2
import webapp2
import json
from models import Message
from google.appengine.api import users
from google.appengine.api import urlfetch


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))



class MainHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            login = True
            logout_url = users.create_logout_url("/")
            params = {"login": login, "logout_url": logout_url, "user": user}
        else:
            login = False
            login_url = users.create_login_url("/")
            params = {"login": login, "login_url": login_url, "user": user}
        return self.render_template("login.html", params=params)

class InboxHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        messages = Message.query(Message.recipient == user.email()).fetch()
        params = {"messages": messages, "user": user}
        return self.render_template("inbox.html", params=params)

class ComposeHandler(BaseHandler):
    def get(self):
        return self.render_template("compose.html")

    def post(self):
        sender = self.request.get("sender")
        recipient = self.request.get("recipient")
        subject = self.request.get("subject")
        message = self.request.get("message")

        composed_message = Message(sender=sender, recipient=recipient, subject=subject, message=message)
        composed_message.put()
        return self.render_template("success.html")

class SentMailHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        messages = Message.query(Message.sender == user.email()).fetch()
        params = {"messages": messages, "user": user}
        return self.render_template("sent-mail.html", params=params)

class WeatherHandler(BaseHandler):
    def get(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=Ljubljana,si&units=metric&APPID=a0241b9bbba3222fa6227f5a94479988"
        result = urlfetch.fetch(url)
        data = json.loads(result.content)
        params = {"data": data}
        self.render_template("weather.html", params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/inbox', InboxHandler),
    webapp2.Route('/compose', ComposeHandler),
    webapp2.Route('/sent-mail', SentMailHandler),
    webapp2.Route('/weather', WeatherHandler),
], debug=True)
