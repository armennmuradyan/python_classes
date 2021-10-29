import json
import requests
with open("json_file.json", "r") as json_file:
    data = json.load(json_file)


for obj in data:
    response = requests.get(obj["img_url"])
    names = obj["img_name"]
    with open(names, "wb") as photo:
        photo.write(response.content)
