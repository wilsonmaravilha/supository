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
class AdminHandler(BaseHandler):

	# Do the normal home render page
	def get(self):

		crafter_obj = schema.Crafter()
		crafter_obj.name = 'Someone'
		crafter_obj.put()

		crafters = schema.Crafter.get_all()
		# Locales
		locales = {
			'crafters': crafters
		}

		# Render the template
		self.render('admin.html', locales)

class EditCrafterHandler(BaseHandler):
	def get(self, id):
		crafter = schema.Crafter.get_crafter(id)
		locales = { "crafter" : crafter}
		self.render('editcrafter.html', locales)
	def post(self):
		pass
