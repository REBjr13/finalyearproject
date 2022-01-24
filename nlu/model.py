import yaml
import os
import json

with open(r'C:\Users\pc\Desktop\hello\nlu\train.yaml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

inputs, outputs = [], []

for command in data['commands']: 
    input.append(command['input'])
    outputs.append('{}\{}'.format(command['entity'], command('action')))
    
print(inputs)
print(outputs)