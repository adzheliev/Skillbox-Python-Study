import requests
import json


my_req = requests.get('https://www.breakingbadapi.com/api/deaths')
data = json.loads(my_req.text)

max_death_count = 0
for elem in data:
    if elem['number_of_deaths'] > max_death_count:
        max_death_count = elem['number_of_deaths']

for elem in data:
    if elem['number_of_deaths'] == max_death_count:
        print(elem)
        with open('most_deadful_episode.json', 'w') as file:
             json.dump(elem, file, indent=4)