
import json


test_olly = '''{
    "ecom": {
        "classic": {
            "names": ["flipkart", "snapdeal", "paytmmall", "zopper"],
            "score": 5
        },
        "premium": {
            "names": ["amazonshopping", "amazonprime", "myntra", "netflix", "hotstar", "bookmyshow"],
            "score": 10
        }
    },
    "fintech": {
        "classic": {
            "names": ["paytm", "mobikwik", "freecharge", "oxigen"],
            "score": 5
        },
        "premium": {
            "names": ["tez", "bhim", "chillr"],
            "score": 20
        }
    },
    "social": {
        "classic": {
            "names": ["whatsapp", "facebook", "instagram", "snapchat"],
            "score": 5
        },
        "premium": {
            "names": ["pinterest", "quora", "tumblr", "skype", "slack", "twitter"],
            "score": 10
        }
    },
    "utility": {
        "classic": {
            "names": ["zomato", "olacabs"],
            "score": 5
        },
        "premium": {
            "names": ["uber", "swiggy", "grofers", "bigbasket", "oyo", "urbanclap"],
            "score": 10
        }
    }
}
'''

test1 = json.loads(test_olly)
# print(test1)
print(type(test1))  # json strings prints as dictionaries when converted to an object
print(type(test1["ecom"]["classic"]['score']))

# for x in test1:
#  print(x)

for x in test1["ecom"]["classic"]:
  print(x)

# for x in test1['classic']['name']:
#  print x

#--------------------------------------------------------------------------------------------------------->

state_str = '''{
    "states": [
        {
            "name": "Alabama",
            "abbreviation": "AL",
            "area_codes": ["205", "251", "256", "334", "938"]
        },
        {
            "name": "Alaska",
            "abbreviation": "AK",
            "area_codes": ["907"]
        },
        {
            "name": "Arizona",
            "abbreviation": "AZ",
            "area_codes": ["480", "520", "602", "623", "928"]
        }
    ]
}
  '''


test2 = json.loads(state_str)

print(type(test2))
print(type(test2['states']))

for x in test2['states']:  # since test2['states'] is a list we can simply loop through it
  # print(x)  # now each of these 3 attribute in array are dict, we can simply take out values against the keys for them.
  # print(x)
  print(x)


# loading a python object into a json

new_string = json.dumps(test2, indent=2, sort_keys=True)
print(new_string)

#---------------------------------------------------------------------->
# loading a JSON file into python object

import json

with open('states.json') as f:
data = json.load(f)

for state in data['states']:
del state['area_codes']

with open('new_states.json', 'w') as f:
json.dump(data, f, indent=2)


#------------------------------------------------------------------------->
import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))
#---------------------------------------------

import json


class Object:


def toJSON(self):
  return json.dumps(self, default=lambda o: o.__dict__,
                    sort_keys=True, indent=2)


me = Object()
me.name = "Onur"
me.age = 35
me.dog = Object()
me.dog.name = "Apollo"

print(me.toJSON())

#---------------------------------------------------------
from json import JSONEncoder

f = '{"fname": "/foo/bar"}'


class MyEncoder(JSONEncoder):
  def default(self, o):
    return o.__dict__


MyEncoder().encode(f)
json.dumps(cls=MyEncoder)
