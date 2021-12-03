import json
import requests
import csv

import urllib, json
#Sensory

open('venv/sensory.json', 'w').close()

stationId = str(0)
lista = ['4769','4772']
for id in (lista):
    url = ("https://api.gios.gov.pl/pjp-api/rest/data/getData/" + id)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    r = requests.get('https://api.gios.gov.pl/pjp-api/rest/data/getData/' + id)
    r.status_code

    r.headers['content-type']
    'application/json; charset=utf8'
    r.encoding
    'utf-8'
    r.text
    '{"type":"User"...'
    r.json()

    with open('venv/sensory.json', 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)






#konwertowanie do csv

    with open("venv/sensory.json") as file:
        data = json.load(file)

    with open("venv/data.csv", "w") as file:
        csv_file = csv.writer(file)
        for item in data:
            fields = list(item['values'].values())
            csv_file.writerow([item['key']] + fields)

'''
with open('sensory.json') as json_file_sensor:
    data = json.load(json_file_sensor)

sensors_data = data['key']

# now we will open a file for writing
data_file = open('data_sensors.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for sen in sensors_data:
    if count == 0:
        # Writing headers of CSV file
        header = sen.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(sen.values())

data_file.close()
'''