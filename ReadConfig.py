import json

with open('config.json') as config_file:
    data = json.load(config_file)

firstConfigSet = data['firstConfigSet']
secondConfigSet = data['secondConfigSet']

#read the dictionary of key and values
for keys1 in firstConfigSet.keys():
   print(keys1, firstConfigSet[keys1])

#read the dictionary of key and values
for keys2 in secondConfigSet.keys():
   print(keys2, secondConfigSet[keys2])