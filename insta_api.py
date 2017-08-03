#A small web app for searching multiple tags on instagram

from instagram.client import InstagramAPI

import settings
#settings.py includes the following:
	# client_id = ""
	# client_secret = ""
	# access_token = ""

from instagram.client import InstagramAPI

api = InstagramAPI(access_token=access_token, client_secret=client_secret)
print api.tag_search(q='sdzoo', count=10)