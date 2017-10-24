#A small web app for searching multiple tags on instagram
#Takes input in the form of a list of tags, returns oembed code for displaying
#images on a webpage

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
def get_image_links(tag_name):
	endpoint_url = "/v1/tags/" + tag_name + '/media/recent'
	request_url = base_url + endpoint_url + "?access_token=" + access_token

	api_return = requests.get(request_url)
	if api_return.status_code == 200: #healthy response
		response_dict = api_return.json()
		num_images = len(response_dict['data'])
		image_links = []
		# print response_dict['data']
		for image in response_dict['data']:
			image_links.append(image['link'])
		return image_links
		# with open('json_response.json', 'w') as fd:
		# 	json.dump(api_return.json(), fd, indent=4, sort_keys=True)
		# 	fd.close()
	else:
		print('failure, returned: ' + str(api_return.status_code))

#GET image oembed code
#Return oembed code (does not require access_token)
# https://instagram.com/p/fA9uwTtkSN/media/?size=t
def get_media_file(image_link):
	request_url = image_link + 'media/?size=m'

	api_return = requests.get(request_url)

	if api_return.status_code == 200: #healthy response
		return api_return.text
	else:
		print('failure getting media file, returned: ' + str(api_return.status_code))

def run_xtratag(*tags):
	picture_id_dict = defaultdict(list) #create dictionary with key=image_id, value=list of tags
	for tag in tags:
		link_list = get_image_links(tag)
		for link in link_list:
			picture_id_dict[link].append(tag)

	media_files = [] #list of images to be returned
	for image_link, matched_tags in picture_id_dict.items():
		if len(matched_tags) == len(tags):
			# media_files.append(get_media_file(image_link))
			media_files.append(image_link + 'media/?size=m')
	return media_files