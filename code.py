import pandas as pd
import requests as req
import json
import urllib.request


URL = 'https://xy5w32z11f.execute-api.ap-south-1.amazonaws.com/animals_pic'
PAYLOAD = {'keyword':'dog'}

r = req.get(URL, params = PAYLOAD, timeout=5)
r = r.json()
url = r['image_url']

response = req.get(url)

    # Save the image
file_name ='imagepdsfp.jpg'
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
else:
    print(response.status_code)
