import json as j
python_data = {'monty': 'garo', 'nitin': 'lost in somewhere'}
dop = j.dumps(python_data)
print(dop)
print(type(dop))
lod = j.loads(dop)
print(lod)
print(type(lod))

# note - json data always in two inverted commas
json_data = {"monty": "garo"}  # getting error beacue json data is not string
ldy = j.loads(json_data)
print(type(ldy))
print(ldy)
