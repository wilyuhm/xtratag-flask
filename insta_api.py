#A small web app for searching multiple tags on instagram

import requests
import json
from collections import defaultdict

import settings
#settings.py includes the following:
client_id = settings.client_id
client_secret = settings.client_secret
access_token = settings.access_token

base_url = "https://api.instagram.com"

#GET Tags/tag-name/media/recent
#Return list of image_ids
def get_image_ids(tag_name):
	endpoint_url = "/v1/tags/" + tag_name + '/media/recent'
	request_url = base_url + endpoint_url + "?access_token=" + access_token

	api_return = requests.get(request_url)

	if api_return.status_code == 200: #healthy response
		response_dict = api_return.json()
		num_images = len(response_dict['data'])
		image_ids = []
		# print response_dict['data']
		for image in response_dict['data']:
			image_ids.append(image['id'])
		return image_ids
		# with open('json_response.json', 'w') as fd:
		# 	json.dump(api_return.json(), fd, indent=4, sort_keys=True)
		# 	fd.close()
	else:
		print('failure, returned: ' + str(api_return.status_code))

tags = ['stilts', 'sdzoo', 'jumpingstilts']
picture_id_dict = defaultdict(list)
for tag in tags:
	id_list = get_image_ids(tag)
	for id in id_list:
		picture_id_dict[id].append(tag)

print picture_id_dict