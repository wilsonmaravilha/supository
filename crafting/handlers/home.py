# Google Apis
from google.appengine.api import users
from google.appengine.api.logservice import logservice
from webapp2_extras import sessions

# Custom importing
from base import BaseHandler
import crafting.schema as schema

#
# Acts as the Frontpage when users are not signed in and the dashboard when they are.
# @author Johann du Toit
#
class HomepageHandler(BaseHandler):

	# Do the normal home render page
	def get(self):

		crafter_obj = schema.Product()
		crafter_obj.name = 'Other Pengiun'
		crafter_obj.summary = 'Hand Built Wire Pengiun'
		crafter_obj.price = '100.00'
		crafter_obj.description = "It's a real thing. Yes I know ...."
		# crafter_obj.put()

		# Get the list for the homepage
		crafters = schema.Crafter.get_for_homepage()
		products = schema.Product.get_newest_for_homepage()

		# Locales
		locales = {

			"title": "Welcome",
			"crafters": crafters,
			'products': products

		}

		# Render the template
		self.render('home.html', locales)