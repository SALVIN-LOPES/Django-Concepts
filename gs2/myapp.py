# sending : data --> json
# CLIENT FRONTEND :

import requests
import json
URL  = "http://127.0.0.1:8000/student-create/"
# python dictionary -->
data = {
    'name' : 'salvin lopes',
    'roll' : 101,
    'city' : 'mumbai'
}

# json data -->
json_data = json.dumps(data) 
# post request -->
r = requests.post(url = URL,data = json_data)
# Extracting data -->
data = r.json()
print(data)