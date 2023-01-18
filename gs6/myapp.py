import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"
def get_data(id = None):
    data = {}
    if id is not None : #id exists
        data = {"id":id} # python dictionary
    json_data = json.dumps(data)
    r = requests.get(url = URL,data = json_data)
    # Extracting the response r : 
    data = r.json()
    print(data)

# get_data()

def post_data():
    # sending data to backend --> django
    # python dictionary
    data = {
        'name': 'ian lopes',
        'roll' : 105, 
        'city' : 'canada'
    }
    json_data = json.dumps(data) # json data
    r = requests.post(url = URL,data = json_data) # sending request
    data = r.json() # extracting response
    print(data)

# post_data()

def update_data():
    # sending data to backend --> django
    # python dictionary
    data = {
        'id' : 4,
        'name': 'salvin lopes',
        'roll' : 102,
        'city' : 'mumbai'
    }
    json_data = json.dumps(data) # json data
    r = requests.put(url = URL,data = json_data) # sending request
    data = r.json() # extracting response
    print(data)

# update_data()

def delete_data():
    # sending data to backend --> django
    # python dictionary
    data = { 'id': 5 }

    json_data = json.dumps(data) # json data
    r = requests.delete(url = URL,data = json_data)
    # Extracting the response r : 
    data = r.json()
    print(data)

delete_data()


