# 10/08/2019


# to create a virtual enviroment: py -m venv <enviromentNameHere>
# to activate virtual enviroment:
#         Windows:  <enviromentNameHere>/Scripts/activate

# to verify: terminal should hace the virt-env on the left #  (my_super_cool_enviroment) PS C:\Users\JimRB\Desktop\Python October\workspace\PythonFundamentals>
# pip install requests

import requests

response = requests.get("https://api.spacexdata.com/v3/rockets")

print(response)  # prints code ie error code 404 or 200

data = response.json() 
# print(data) 
for entry in data:
    # print(entry.keys(),"\n")
    print(entry['rocket_name'], "\n")

    https://rickandmortyapi.com/api/character/2

import pprint

import requests

import time
start = time.time()


# response = requests.get("https://rickandmortyapi.com/api/character/5") # the below but all in one line
api_url = "https://rickandmortyapi.com/api/"  #base api
character_response = requests.get(api_url + "character")
# print(response)  # prints code ie error code 404 or 200
try:
    data = character_response.json() # json takes return from request and tries to turn into dictionary or list
except Exception:
    data = None


# print(type(data)) # will print what type od data will print in data
print(data.keys())
print(data['info'])

print(data['info']['count'])  # this will return all of the entries 


try:
    data = character_response.json() # json takes return from request and tries to turn into dictionary or list
except Exception:
    data = None


choices = data['info']['count']

choice = input(f' Pick a character from 1  and { choices } >> ') # input from user and formating

chosen = requests.get(api_url + "character/" + choice )

chosen_one = chosen.json()


print(chosen.headers)
print(chosen_one['name'])

# data = character_response.json() 
# # print(data.keys() ,"\n") #this tells you all the dictionary keys avaliable at that level
# print(data['name'], "\n") # prints just the 'name' for that api character 2
# print(data['episode'], "\n")
# # print(data.values() ,"\n") 

#have no idea why you would want a for loop here
# for entry in data:
#     # print(data.keys(),"\n")
#     print(data['name'], "\n")


end = time.time()
print('Time taken to run: ', end - start, 'seconds')