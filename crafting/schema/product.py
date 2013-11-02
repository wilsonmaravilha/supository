# Google Libraries
from google.appengine.ext import ndb
from google.appengine.api.logservice import logservice
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.api import images

from crafter import Crafter

# Python Libs
import datetime
import logging


class Product(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add=True)
	lastupdated = ndb.DateTimeProperty(auto_now_add=True)
	crafter = ndb.KeyProperty(kind=Crafter)
	materials = ndb.StringProperty()
	name = ndb.StringProperty()
	summary = ndb.StringProperty()
	description = ndb.TextProperty()
	price = ndb.StringProperty()

	#
	# Returns the event by it's slug
	#
	@staticmethod
	def get_newest_for_homepage():

		query_obj = Product.query()
		return query_obj.fetch(limit=6)

