# Google Libraries
from google.appengine.ext import ndb
from google.appengine.api.logservice import logservice
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.api import images

# Python Libs
import datetime
import logging

#
# Event Details
# @author Johann du Toit
#
class Crafter(ndb.Model):
	name = ndb.StringProperty()
	surname = ndb.StringProperty()
	id_number = ndb.StringProperty()
	cell_number = ndb.StringProperty()
	website = ndb.StringProperty()
	email = ndb.StringProperty()
	province = ndb.StringProperty()
	town = ndb.StringProperty()
	suburb = ndb.StringProperty()
	location = ndb.GeoPtProperty()
	organization = ndb.GeoPtProperty()
	active = ndb.BooleanProperty(default=False)
	lastupdated = ndb.DateTimeProperty(auto_now_add=True)
	created = ndb.DateTimeProperty(auto_now_add=True)

	#
	# Returns the event by it's slug
	#
	@staticmethod
	def get_crafters_for_homepage():

		query_obj = Crafter.query()
		return query_obj.fetch()

