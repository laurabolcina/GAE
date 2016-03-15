#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import GuestMessage


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
        return self.render_template("index.html")

class GuestPostHandler(BaseHandler):
    def get(self):
        return self.render_template("new-message.html")

    def post(self):
        guest_name = self.request.get("name")
        if guest_name == "":
            guest_name = "Guest"
        guest_surname = self.request.get("surname")
        guest_email = self.request.get("email")
        guest_message = self.request.get("message")

        guest_post = GuestMessage(name=guest_name, surname=guest_surname, email=guest_email, message=guest_message)
        guest_post.put()
        return self.write("Message successfully added to the guestbook.")

class GuestBookHandler(BaseHandler):
    def get(self):
        messages = GuestMessage.query(GuestMessage.deleted == False).fetch()
        params = {"messages": messages}
        return self.render_template("guestbook.html", params=params)

class MessageHandler(BaseHandler):
    def get(self, message_id):
        guest_post = GuestMessage.get_by_id(int(message_id))
        params = {"guest_post": guest_post}
        return self.render_template("message.html", params=params)

class EditMessageHandler(BaseHandler):
    def get(self, message_id):
        guest_post = GuestMessage.get_by_id(int(message_id))
        params = {"guest_post": guest_post}
        return self.render_template("edit-message.html", params=params)

    def post(self, message_id):
        new_message = self.request.get("message")
        guest_post = GuestMessage.get_by_id(int(message_id))
        guest_post.message = new_message
        guest_post.put()
        return self.redirect_to("guestbook")

class DeleteMessageHandler(BaseHandler):
    def get(self, message_id):
        guest_post = GuestMessage.get_by_id(int(message_id))
        params = {"guest_post": guest_post}
        return self.render_template("delete-message.html", params=params)

    def post(self, message_id):
        guest_post = GuestMessage.get_by_id(int(message_id))
        guest_post.deleted = True
        guest_post.put()
        return self.redirect_to("guestbook")

class AdminHandler(BaseHandler):
    def get(self):
        messages = GuestMessage.query(GuestMessage.deleted == True).fetch()
        params = {"messages": messages}
        return self.render_template("admin.html", params=params)

class AdminRestoreHandler(BaseHandler):
    def post(self, message_id):
        guest_post = GuestMessage.get_by_id(int(message_id))
        guest_post.deleted = False
        guest_post.put()
        return self.write("Message successfully restored.")

class AdminDeleteHandler(BaseHandler):
    def post(self, message_id):
        guest_post = GuestMessage.get_by_id(int(message_id))
        guest_post.key.delete()
        return self.write("Message permanently deleted.")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/new-message', GuestPostHandler),
    webapp2.Route('/guestbook', GuestBookHandler, name="guestbook"),
    webapp2.Route('/message/<message_id:\d+>', MessageHandler),
    webapp2.Route('/message/<message_id:\d+>/edit', EditMessageHandler),
    webapp2.Route('/message/<message_id:\d+>/delete', DeleteMessageHandler),
    webapp2.Route('/admin', AdminHandler, name="admin"),
    webapp2.Route('/message/<message_id:\d+>/restore', AdminRestoreHandler),
    webapp2.Route('/message/<message_id:\d+>/permanently-delete', AdminDeleteHandler),
], debug=True)
