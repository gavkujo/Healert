import json

x = "hndnndnd"

with open("userfiles.json", "r") as jsonFile:
    data = json.load(jsonFile)

data["username"] = x

with open("userfiles.json", "w") as jsonFile:
    json.dump(data, jsonFile)