# Google Libraries
from google.appengine.ext import db
from google.appengine.api.logservice import logservice
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.api import images

# Python Libs
import datetime
import logging


class Product(db.Model):
	created = db.DateTimeProperty(auto_now_add=True)
	lastupdated = db.DateTimeProperty(auto_now_add=True)
	crafter = db.ReferenceProperty(Crafter)
	materials = db.StringProperty()
	price = db.StringProperty()

