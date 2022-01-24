import yaml
import os
import json

data = yaml.safe_load(open('nlu\\train.yaml').read())

inputs, outputs = [], []

for command in data['commands']: 
    input.append(command['input'])
    #outputs.append('{}\{}'.format(command['entity'], command('action')))
    
print(inputs)
#print(outputs)