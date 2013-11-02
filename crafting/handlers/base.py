# Google Apis
from google.appengine.api import users
from google.appengine.api.logservice import logservice
from webapp2_extras import sessions
import webapp2
import jinja2

# Python Apis
import os
import os
import time
import logging

# Setup our Jinja Runner
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('views'))

#
# Acts as the Frontpage when users are not signed in and the dashboard when they are
#
class BaseHandler(webapp2.RequestHandler):

	# Has not run !
	has_setup_run = False

	# Return True or False
	# wether the user is logged in
	# or not
	def is_logged_in(self):

		# Just a quick return
		return 'logged_in_user_id' in self.session and self.session['logged_in_user_id'] != None

	@webapp2.cached_property
	def session(self):
		# Returns a session using the default cookie key.
		return self.session_store.get_session()

	def setup(self):

		# Run setup if not already run !
		if self.has_setup_run is False:
			self.has_setup_run = True

	# Do some general checks
	# here we mostly just check users
	def dispatch(self):

		self.setup()

	# Our global key to check for if
	# a site comes in
	viewing_site_key = None

	# Our defaults
	defaults = {

		'title': False,
		'description': False,
		'keywords': False,
		'author': False,
		'errors': []

	}

	#
	# Merges and returns the template vars.
	# Just a quick util method
	#
	def get_default_template_vars(self, current_vars={}):

		# current default vars
		default_vars = self.defaults

		# Check if production
		is_production = os.environ['SERVER_SOFTWARE'].startswith('Dev')
		rev_uuid_valid = os.environ['dist_rev'] != None and len(os.environ['dist_rev']) > 0

		# Set posted items
		post_params = {}
		for key in self.request.POST.keys():

			# Set by key
			post_params[key] = self.request.POST.get(key)

		# Set as view option
		default_vars['post_params'] = post_params

		# Setup generated defaults and check if running on server
		if not is_production and rev_uuid_valid:

			# Setup default
			default_vars['rev_uuid'] = os.environ['dist_rev']
			default_vars['rev_uuid_ext'] = '-' + default_vars['rev_uuid'] + '.min'

		else:

			# Default to blank !
			default_vars['rev_uuid'] = ''
			default_vars['rev_uuid_ext'] = ''

		# Add logged in user details if saved in session
		if 'logged_in_user_id' in self.session and self.session['logged_in_user_id'] != None:

			# Set our logged in user to use for the view
			default_vars['logged_in_user'] = {

				'id': self.session['logged_in_user_id'],
				'name': self.session['logged_in_user_name'],
				'email': self.session['logged_in_user_email']

			}

		else:

			# False user !
			default_vars['logged_in_user'] = False

		# Return merged collections
		return dict(default_vars.items() + current_vars.items())


	#
	# Wrapper for output
	#
	def send(self, output_str):
		self.response.out.write(output_str)

	#
	# Quick definition wrapper to output the sent template
	#
	def render(self, template_str, template_vars=None):
		template_vars = self.get_default_template_vars(template_vars)
		template = jinja_environment.get_template(template_str)
		self.response.out.write(template.render(template_vars))
	
