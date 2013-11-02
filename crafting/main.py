#!/usr/bin/env python

# Python Libs
import os
import sys
import urllib

# Google Apis
import webapp2
from webapp2_extras import routes

from crafting.handlers.home import HomepageHandler
from crafting.handlers.product import ProductHandler
from crafting.handlers.auth import LoginHandler, LogoutHandler
from crafting.handlers.crafters import CraftersHandler
from crafting.handlers.admin import AdminHandler, EditCrafterHandler

# General Config for our web application
config = {}
config['webapp2_extras.sessions'] = {

    'secret_key': 'secret_key_for_session_here'

}

# Setup with our little path fix trick
# sys.path.append(os.path.join(os.path.dirname(__file__), 'hubspot'))

# Startup our app with the routes we are
# going to configure now
app = webapp2.WSGIApplication([

	('/', HomepageHandler),
	('/login', LoginHandler),
	('/logout', LogoutHandler),
	webapp2.Route(r'/p/<product_id:\d+>/<product_name:\s+>', handler=ProductHandler),
	('/admin', AdminHandler),
	('/editCrafter/key=(.*)', EditCrafterHandler)
	('/crafters.json', CraftersHandler)

], debug=True, config=config)
