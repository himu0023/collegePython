import json

x = '{"name":"optimus prime", "planet": "cybertron", "alterego":"nemesis prime"}'

print(x)

y = json.loads(x)

print(y['alterego'])