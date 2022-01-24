import yaml
import os
import json

data = yaml.safe_load(open('nlu\\train.yaml').read())

for command in data['commands']:
    print(command)

#with open(r'C:\Users\pc\Desktop\hello\nlu\train.yaml') as file:
 #   train_list = yaml.load(file, Loader=yaml.FullLoader)
    
   # print(train_list)