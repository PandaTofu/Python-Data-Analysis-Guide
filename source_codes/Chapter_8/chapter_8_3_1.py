import json

json_str = """

py_obj = json.loads(json_str)

py_obj

json.dumps(py_obj)

cat examples/example_6_11.json

with open('examples/example_6_11.json') as fo:
    py_obj = json.load(fo)

py_obj

with open('examples/json_export.json', 'w') as fo:
    json.dump(py_obj, fo)

cat examples/json_export.json

