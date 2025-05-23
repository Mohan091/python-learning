import json 
import csv 

with open("output.json",'r') as jsonfile:
    data = json.load(jsonfile)
    rows = data

with open("test.csv",'w') as csvfile:
    headers = rows[0].keys()
    csvwriter = csv.DictWriter(csvfile,fieldnames=headers)
    csvwriter.writeheader()
    csvwriter.writerows(rows)