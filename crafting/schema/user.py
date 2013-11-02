# Google Libraries
from google.appengine.ext import ndb
from google.appengine.api.logservice import logservice
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.api import images

# Python Libs
import datetime
import logging

# Custom Libs
from crafting.schemas.base import BaseModel

#
# Represents a user in the system
# this user can either just buy tickets
# or by invited to talk at a event
#
# @author Johann du Toit
#
class User(BaseModel):
	avatar = ndb.StringProperty()
	session_counts = ndb.IntegerProperty()
	session_like_counts = ndb.IntegerProperty()
	session_last_talk = ndb.DateTimeProperty()
	name = ndb.StringProperty()
	email = ndb.StringProperty()
	description = ndb.TextProperty()
	created = ndb.DateTimeProperty(auto_now_add=True)
	lastupdated = ndb.DateTimeProperty(auto_now_add=True)

	#
	# Returns the account by it's e-mail
	#
	@staticmethod
	def get_by_email(email_str):

		query_obj = User.query(User.email == email_str)
		return User.get_single_result(query_obj)

#
# Every user can have multiple accounts
# this is for logging in. But also for
# people like speakers to have their
# accounts listed
#
# @author Johann du Toit
#
class Account(BaseModel):
	user = ndb.KeyProperty(kind=User)
	avatar = ndb.StringProperty()
	name = ndb.StringProperty()
	password = ndb.StringProperty()
	uid = ndb.StringProperty()
	email = ndb.StringProperty()
	provider = ndb.StringProperty()
	data = ndb.JsonProperty()
	created = ndb.DateTimeProperty(auto_now_add=True)
	lastupdated = ndb.DateTimeProperty(auto_now_add=True)

	#
	# Returns the account by it's e-mail
	#
	@staticmethod
	def get_by_email(email_str):

		query_obj = Account.query(Account.email == email_str)
		return query_obj.fetch()

	#
	# Checks and returns the account_obj for that
	# provider
	#
	@staticmethod
	def get_by_provider_uid(provider, uid):

		query_obj = Account.query(Account.uid == uid).query(Account.provider == provider)
		return query_obj.fetch()

	#
	# Returns account's that have been linked
	# to a certain user
	#
	@staticmethod
	def get_by_user(user_obj):

		query_obj = Account.query(Account.user == user_obj)
		return query_obj.fetch()

