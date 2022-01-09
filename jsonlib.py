import json

data = '{"var1":"shahid", "var2":"hammad"}'
print(data)
parsed = json.loads(data)
print(parsed['var1'])
print(type(parsed))

data2 = {
    "channel_name": "shahid developer",
    "cars": ['bmw', 'ferrari', 'audi'],
    "bag": ('laptop', 'keys', 5)
}
jscomp = json.dumps(data2)
print(jscomp)