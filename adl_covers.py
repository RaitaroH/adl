#!/usr/bin/env python3

import requests
from os.path import exists
from os.path import join
import sys
import tempfile

# Catch if user didn't give argument
if len(sys.argv) > 1:
    list = sys.argv[1:]
else:
    print("Usage:", sys.argv[0], "'title1' 'title2' [...]")
    print("Title not specified. Exiting.")
    quit()

query = '''
query ($id: Int, $search: String) {
	Media (id: $id, search: $search, type: ANIME) {
		id
		coverImage {
			large
		}
	}
}
'''
api = 'https://graphql.anilist.co'

for title in list:
	file = join(tempfile.gettempdir(), title + '.png')
	if exists(file):
		continue
	response = requests.post(api, json={'query': query, 'variables': {'search': title}})
	url = response.json()['data']['Media']['coverImage']['large']
	# retrieving data from the URL using get method
	r = requests.get(url)
	open(file, 'wb').write(r.content)
