# It's a third parth app which will be requesting the data from the django backend.....
# FRONT END DATA ACCESSIBLE : Seperate application

import requests


URL = "http://127.0.0.1:8000/student/2"

r = requests.get(url = URL)

data = r.json()

print(data)


