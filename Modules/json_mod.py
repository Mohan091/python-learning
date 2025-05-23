import json 

#Json 
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# dict 
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# Json to python converion 

# test = json.loads(x)

# print(test["city"])


# Python to json conversion
test = json.dumps(x)
with open("test.json",'w') as file:
    file.write(test)