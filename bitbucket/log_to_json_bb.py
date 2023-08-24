import argparse

parser = argparse.ArgumentParser(description='FILENAME: path to your imported-targets.log')
parser.add_argument("--filename")

args = parser.parse_args()
filename = args.filename

import json

def create_json():

	result = []
	with open(f"{filename}") as log_file:
		for jsonObj in log_file:
			data = json.loads(jsonObj)
			result.append(data)

	all_content = []
	for key in result:
		content = dict()

		content['orgId'] = key["orgId"]
		content['integrationId'] = key["integrationId"]

		target = dict()
		target['repoSlug'] = key["target"]["repoSlug"]
		target['name'] = key["target"]["projectKey"]
		target['projectKey'] = key["target"]["projectKey"]
		content['target'] = target

		all_content.append(content)

		unique = list({ repr(each): each for each in all_content }.values())

	return unique 

## Defines import file
fname = 'import-projects.json'

## Creates file with appropriate content
with open(fname, 'w') as outfile:
  outfile.write('{"targets":')

with open(fname, 'a') as outfile:
	json.dump(create_json(), outfile)

## Closes off file with appropriate JSON
with open(fname, 'ab') as outfile:
	outfile.seek(-1, 2)
	outfile.truncate()

with open(fname, 'a') as outfile:	
	outfile.write(']}')