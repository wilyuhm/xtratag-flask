#A small web app for searching multiple tags on instagram

import requests
import settings
#settings.py includes the following:
client_id = settings.client_id
client_secret = settings.client_secret
access_token = settings.access_token

base_url = "https://api.instagram.com"
tag_name = 'sdzoo'
endpoint_url = "/v1/tags/" + tag_name
request_url = base_url + endpoint_url + "?access_token=" + access_token

api_return = requests.get(request_url)

if api_return.status_code == 200:
	print api_return.text
else :
	print 'failure, returned: ' + str(api_return.status_code)