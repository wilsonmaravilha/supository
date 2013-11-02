# Google Apis
from google.appengine.api import users
from google.appengine.api.logservice import logservice
from webapp2_extras import sessions

# Libraries
import webapp2

#
# Login with your Google Account
# @author Johann du Toit
#
class LoginHandler(webapp2.RequestHandler):
	def get(self):

		# Normal Google User Account
		self.redirect(users.create_login_url('/'))


#
# Logout from your Google Account
# @author Johann du Toit
#
class LogoutHandler(webapp2.RequestHandler):
	def get(self):

		# Send to logout
		self.redirect(users.create_logout_url('/'))

