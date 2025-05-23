import json 
import csv 

data = {"Names": []}

with open("username.csv", 'r', encoding ='latin-1') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=";")
    next(csvreader)
    for row in csvreader: 
        if all(cell.strip() == "" for cell in row):  #skip the empty cells if any
            continue
        data["Names"].append({"Username":row[0], "Identifier": row[1], "Firstname": row[2], "Lastname":row[3]})

with open("output1.json",'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)        