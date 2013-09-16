
# Google App Engine Libs
from google.appengine.ext import db
from google.appengine.api.logservice import logservice
from webapp2_extras import sessions

# Python Libs
import logging
import time
import calendar
import uuid

# Custom Libs
import schemas

#
# Creates a token and returns the session object.
# More like a global hook.
# @author Johann du Toit
#
def return_and_global_session_update(request_class):

	# Get the session store and session
	session_store = sessions.get_store(request=request_class.request)
	session = session_store.get_session()

	# Check if token in the session
	if 'search_token' not in session:
		session['search_token'] = str(uuid.uuid1())

	# Save the session
	session_store.save_sessions(request_class.response)

	# Return the session.
	return session

#
# Parse out searches according to year in a week format.
# The result returned is a list of weeks and their stats
# @author Johann du Toit
#
def parse_out_weeks(year, stats):

	# Defaults and lists to return
	week_count = 1

	# Loop all 12 months
	for month in range(1, 13):

		# Get the mondays for that month
		mondays = [ day.split()[0] for day in calendar.month(year, month).split("\n")[2:-1] if not day.startswith("  ")]

		# Loop each monday and check for search in that week.
		for monday in mondays:

			# Contruct info object
			week_obj = {}
			week_obj['date'] = "%i-%02i-%02i" % (year, int(month), int(monday))

			# Defaults. All 0 naturally
			week_obj["total"] = 0
			week_obj["found"] = 0
			week_obj["failure"] = 0
			week_obj["notfound"] = 0

			# Loop the stats and find the weekly searches
			for stat in stats:

				# Check if the week matches
				if stat.week == week_count and int(stat.total) > 0:

					# if the week matches add the amounts
					week_obj['total'] += int(stat.total)
					week_obj['found'] += int(stat.found)
					week_obj['failure'] += int(stat.failed)
					week_obj['notfound'] += int(stat.notfound)

			# Increment the count of week we are one.
			week_count += 1

			# Was thinking of only adding weeks bigger than 0 but this is the DAL
			# Want to keep logic like that to the upper level.
			yield week_obj


#
# Returns a list of all the cities in the stats and their stats
# These stats are for a entire year !
# @author Johann du Toit
#
def parse_out_cities(stats):

	# Hash of cities
	cities = {}

	# Loop the stats
	for stat in stats:

		# Check if the city was specfied. Just a sanity check ...
		if stat.city is not None:

			# If the city is already in the list
			if stat.city in cities:

				cities[stat.city]['total'] += int(stat.total)
				cities[stat.city]['found'] += int(stat.found)
				cities[stat.city]['failure'] += int(stat.failed)
				cities[stat.city]['notfound'] += int(stat.notfound)

			else:

				# Else create the city entry
				cities[stat.city] = {
					'country': stat.country,
					'total': int(stat.total),
					'found': int(stat.found),
					'failure': int(stat.failed),
					'notfound': int(stat.notfound)
				}

	# Return the hash with stats for each city.
	return cities

#
# Returns a the stats by country.
# @author Johann du Toit
#
def parse_out_countries(stats):

	# The Hash of countries
	countries = {}

	# Loop all the stats
	for stat in stats:

		# Check if the country is present. Just a sanity check ...
		if stat.country is not None:

			# if the country is already added just update the stats
			if stat.country in countries:

				countries[stat.country]['total'] += int(stat.total)
				countries[stat.country]['found'] += int(stat.found)
				countries[stat.country]['failure'] += int(stat.failed)
				countries[stat.country]['notfound'] += int(stat.notfound)

			else:

				# Else we create the country key
				countries[stat.country] = {
					'total': int(stat.total),
					'found': int(stat.found),
					'failure': int(stat.failed),
					'notfound': int(stat.notfound)
				}

	# Return the list of countries
	return countries

#
# Parse and return a object with params that are generated by the specified list of stat
# responses
# @author Johann du Toit
#
def parse_out_general_count(responses):

	# Object template to return
	response_obj = {
		'total': 0,
		'found': 0,
		'notfound': 0,
		'failure': 0
	}

	# Loop and add the values
	for result in responses:

		response_obj['total'] += result.total
		response_obj['found'] += result.found
		response_obj['notfound'] += result.notfound
		response_obj['failure'] += result.failed

	# Return those values
	return response_obj

#
# Returns the Search Stats according to parameters
# @author Johann du Toit
#
def get_stats(kwargs):

	# Query the search counter
	query = schemas.SearchCounter.all()

	# Check if they gave us a week
	if 'week' in kwargs:
		if kwargs["week"] == 'current':
			query.filter("week =", int(time.strftime("%U")))
		else:
			query.filter("week =", int(kwargs["week"]))

	# Check for a Year
	if 'year' in kwargs:
		if kwargs["year"] == 'current':
			query.filter("year =", int(time.strftime("%Y")))
		else:
			query.filter("year =", int(kwargs["year"]))

	# Check for a Provider
	if 'provider' in kwargs:
		query.filter("provider =", kwargs["provider"])

	# Check for Country
	if 'country' in kwargs:
		query.filter("country =", str(kwargs["country"]))

	# Check for City
	if 'city' in kwargs:
		query.filter("city =", str(kwargs["city"]))

	return query

#
# Update or Add to the counter with the country name, city name etc.
# @author Johann du Toit
#
def update_or_add_search_counter(request, result):

	current_week = int(time.strftime("%U"))
	current_year = int(time.strftime("%Y"))

	# Our City Str
	city_str = None
	country_str = None
	region_str = None

	# Set region if present
	if 'X-AppEngine-Region' in request.headers:
		region_str = request.headers['X-AppEngine-Region']

	if 'X-AppEngine-country' in request.headers:
		country_str = request.headers['X-AppEngine-country']

	if 'X-AppEngine-Country' in request.headers:
		country_str = request.headers['X-AppEngine-Country']

	# Set city if present
	if 'X-AppEngine-City' in request.headers:
		city_str = request.headers['X-AppEngine-City']

	puts = []
	for response in result.responses:

		if country_str and city_str:
			# Query List
			query_result = db.GqlQuery("SELECT * FROM SearchCounter WHERE provider=:1 and week=:2 and year=:3 and country=:4 and city=:5 LIMIT 1", response.provider, current_week, current_year, country_str, city_str)
		else:
			# Query List
			query_result = db.GqlQuery("SELECT * FROM SearchCounter WHERE provider=:1 and week=:2 and year=:3 LIMIT 1", response.provider, current_week, current_year)

		counter_obj = None
		if query_result.count() > 0:
			# Update the Value
			counter_obj = query_result.get()
		else:

			# Add Value to database
			counter_obj = schemas.SearchCounter(
				total=0,
				found=0,
				notfound=0,
				failed=0,
				provider=response.provider,
				week = current_week,
				year = current_year,
				city=city_str,
				country=country_str,
				region=region_str
			)

		# Update Values
		counter_obj.total += 1

		if response.status == runner.ProviderResponse.STATUS_FOUND:

			counter_obj.found += 1

		elif response.status == runner.ProviderResponse.STATUS_NOTFOUND:

			counter_obj.notfound += 1

		elif response.status in [runner.ProviderResponse.STATUS_FAILURE, runner.ProviderResponse.STATUS_PARSING]:

			counter_obj.failed += 1

		puts.append(counter_obj)


	# Finish in Background
	return db.put_async(puts)

#
# Returns all the approved providers in the system.
# Used to list the providers in the API, providers page and by the runner
# @author Johann du Toit
#
def approved_providers():
	return db.GqlQuery("SELECT * FROM Provider WHERE approved=True AND tested=True")

#
# Returns all the list of searches by a user.
# @author Johann du Toit
#
def get_user_searches(user, limit_nbr, skip_bnr):

	# Return result
	results = []

	# Returns the listing
	for result in schemas.UserSearch.all().run(offset=skip_bnr,limit=limit_nbr,read_policy=db.EVENTUAL_CONSISTENCY,deadline=5):
		results.append(result)

	# Return the result
	return results

#
# Returns all the registered api clients by a user.
# @author Johann du Toit
#
def get_clients_by_user(user):

	# Get the clients
	clients = db.GqlQuery("SELECT * FROM APIClient WHERE user = :1 AND provider=NULL AND status=True", user)

	# Do a check and return else return a empty list
	if clients is not None:
		return clients
	else:
		return []

#
# Returns all the registered api clients by a provider.
# @author Johann du Toit
#
def get_clients_by_provider(provider):

	# Get the clients
	clients = db.GqlQuery("SELECT * FROM APIClient WHERE provider = :1 AND status=True", provider)

	# Do a check and return else return a empty list
	if clients is not None:
		return clients
	else:
		return []

#
# Returns a Client by it's token
# @author Johann du Toit
#
def client_by_token(token):

	# Build the Query
	client_obj = db.GqlQuery("SELECT * FROM APIClient WHERE token = :1 AND status = True LIMIT 1", token).get()

	# Return Client object
	return client_obj

#
# Returns a list of searches for the specfied provider
# @author Johann du Toit
#
def searches_for_provider(provider, limit_nbr, skip_bnr):

	# Return result
	results = []

	# Get the calls
	calls = db.GqlQuery("SELECT * FROM UserSearchDetail WHERE provider = :1 AND status='found' ORDER BY created DESC", provider)

	# Count
	count = int(calls.count())

	# Search information
	for search_details in calls.run(offset=skip_bnr,limit=limit_nbr,read_policy=db.EVENTUAL_CONSISTENCY,deadline=5):
		results.append(search_details)

	# Return the result
	return (count, results)

#
# Returns a list of searches that were made for a certain UID of which the provider was part of.
# @author Johann du Toit
#
def searches_for_specified_uid(provider, uid, limit_nbr, skip_bnr):

	# Return result
	results = []

	# Get the calls
	calls = db.GqlQuery("SELECT * FROM UserSearchDetail WHERE provider = :1 AND uid = :2 AND status='found' ORDER BY created DESC", provider, uid)

	# count
	count = int(calls.count())

	# Search information
	for search_details in calls.run(offset=skip_bnr,limit=limit_nbr,read_policy=db.EVENTUAL_CONSISTENCY,deadline=5):
		results.append(search_details)

	# Return the result
	return (count, results)

#
# Get the List of Calls made to the search.
# @author Johann du Toit
#
def search_api_calls(client, date, month, year):

	# Get the calls
	calls = db.GqlQuery("SELECT * FROM APICallCount WHERE date = :1 AND month = :2 and year =:3 AND client = :4", date, month, year, client)

	# Do a check and return else return a empty list
	if calls is not None:
		
		return calls

	else:
		return False

#
# Returns a Search by it's Token
# @author Johann du Toit
#
def search_by_token(token):

	# Build the Query
	user_search_obj = db.GqlQuery("SELECT * FROM UserSearch WHERE token = :1 LIMIT 1", token).get()

	# Check if it went fine.
	if user_search_obj is not None:
		user_search_responses = db.GqlQuery("SELECT * FROM UserSearchDetail WHERE search = :1", user_search_obj).run()

	# Else we just add them as a blank list
	else:
		user_search_responses = []

	# Return in a tuple
	return (user_search_obj, user_search_responses)

#
# Returns a provider by it's name
# @author Johann du Toit
#
def provider_by_name(name_str):
	return db.GqlQuery("SELECT * FROM Provider WHERE name = :1 LIMIT 1", name_str)

#
# Delete all the Memberships of a specified user in a specified provider
# @author Johann du Toit
#
def delete_memberships_by_provider(provider, user):
	memberships = db.GqlQuery("SELECT * FROM ProviderMember WHERE user = :1 AND provider = :2", user, provider)
	db.delete(memberships)

#
# Deletes all memberships of a user.
# @author Johann du Toit
#
def delete_memberships(user):

	# Get all the memberships
	memberships = db.GqlQuery("SELECT * FROM ProviderMember WHERE user = :1", user)

	# Delete the memberships
	db.delete(memberships)

#
# Returns all the memberships by a user.
# @author Johann du Toit
#
def memberships_by_user(user):

	# Get the memberships
	memberships = db.GqlQuery("SELECT * FROM ProviderMember WHERE user = :1", user)

	# Do a check and return else return a empty list
	if memberships is not None:
		return memberships
	else:
		return []

#
# Returns a single membership by user and provider.
# @author Johann du Toit
#
def membership_by_user(provider, user):

	# Build and return the membership
	return db.GqlQuery("SELECT * FROM ProviderMember WHERE provider = :1 AND user = :2", provider, user).get()

#
# Returns a list of Members by a Provider
# @author Johann du Toit
#
def memberships_by_provider(provider):

	# Build the Query
	results = db.GqlQuery("SELECT * FROM ProviderMember WHERE provider = :1", provider)
	
	# Check if ok else return empty list
	if results is not None:
		return results
	else:
		return []

#
# Returns a list of membership Keys's by a specified provider
# @author Johann du Toit
#
def get_membership_ids_by_provider(provider):

	# Get the members
	memberships = memberships_by_provider(provider)

	# List of IDS to return
	ids = []

	# Loop all the members and add their keys
	for member in memberships:
		ids.append(member.key())

	# Return the list
	return ids

#
# Returns all Providers that User is a member of.
# @author Johann du Toit
#
def providers_by_user(user):

	 #Get the user memberships
	memberships = memberships_by_user(user)

	# List of providers to return
	providers = []

	# Loop the memberships and add the provider UID to the list of 
	# providers we should return
	for membership in memberships:
		providers.append(membership.provider)

	# Quick sanity check, return blank empty list if not sane.
	if providers is not None:
		return providers
	else:
		return []

#
# Returns a List of Providers, used for the admin section
# @author Johann du Toit
#
def get_list_of_providers():

	# Build the Query
	results = db.GqlQuery("SELECT * FROM Provider ORDER BY created DESC")
	
	# Check if ok else return empty list
	if results is not None:
		return results
	else:
		return []