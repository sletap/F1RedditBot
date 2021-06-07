import requests
import json

NameToID = {
    "Schumacher": "mick_schumacher",
}

# req = requests.get('https://ergast.com/api/f1/2021/6/results.json')
# req = requests.get('http://ergast.com/api/f1/drivers/maxverstappen.json')
req = requests.get('http://ergast.com/api/f1/2021/drivers.json')


print()

print(json.dumps(req.json(), indent=4))