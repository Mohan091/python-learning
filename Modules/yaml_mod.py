import yaml 


# to load yaml in python 
with open("test.yaml",'r') as file:
    # yaml_file=yaml.safe_load(file)
    yaml_file = yaml.safe_load_all(file)  # to load multiple yaml files
    for files in yaml_file:               # to iterate all yaml
        print(files)    


# print(yaml_file)
# print(yaml_file["rest"])    
# print(yaml_file["prime_numbers"][2])


