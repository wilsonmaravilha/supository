# Google Libraries
from google.appengine.ext import db
from google.appengine.api.logservice import logservice
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.api import images

# Python Libs
import datetime
import logging

# Allowed users who may login
# @author Johann du Toit
#
class AllowedUser(db.Model):

	name = db.StringProperty()
	email = db.StringProperty()

	created = db.DateTimeProperty(auto_now_add=True)
	lastupdated = db.DateTimeProperty(auto_now_add=True)

