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
class ProductHandler(BaseHandler):

	# Do the normal home render page
	def get(self, product_id, product_name=False):

		product_obj = schema.Product.get_by_id(product_id)
		if product_obj != None:

			# Locales
			locales = {

				"title": product_obj.name,
				'product_obj': product_obj

			}

			# Render the template
			self.render('product.html', locales)

		else:

			# Redirect to homepage
			self.redirect('/')
