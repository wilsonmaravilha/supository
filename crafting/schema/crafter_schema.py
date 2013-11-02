# Google Libraries
from google.appengine.ext import db
from google.appengine.api.logservice import logservice
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.api import images

# Custom Libraries
import dal

# Python Libs
import datetime
import logging

#
# Event Details
# @author Johann du Toit
#
class Crafter(db.Model):
	name = db.StringProperty()
	surname = db.StringProperty()
	id_number = db.StringProperty()
	cell_number = db.StringProperty()
	website = db.StringProperty()
	email = db.StringProperty()
	province = db.StringProperty()
	town = db.StringProperty()
	suburb = db.StringProperty()
	location = db.GeoPtProperty()
	organization = db.GeoPtProperty()
	active = db.BooleanProperty(default=False)
	lastupdated = db.DateTimeProperty(auto_now_add=True)
	created = db.DateTimeProperty(auto_now_add=True)

class Product(db.Model):
	created = db.DateTimeProperty(auto_now_add=True)
	lastupdated = db.DateTimeProperty(auto_now_add=True)
	crafter = db.ReferenceProperty(Crafter)
	materials = db.StringProperty()
	price = db.StringProperty()


# Allowed users who may login
# @author Johann du Toit
#
class AllowedUser(db.Model):

	name = db.StringProperty()
	email = db.StringProperty()

	created = db.DateTimeProperty(auto_now_add=True)
	lastupdated = db.DateTimeProperty(auto_now_add=True)

