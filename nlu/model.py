import yaml
import os
import json
import numpy as np

data = yaml.safe_load(open('nlu\\train.yaml').read())

#reading the data

inputs, outputs = [], []

for command in data['commands']: 
    inputs.append(command['input'])
    outputs.append('{}\{}'.format(command['entity'], command['action']))
    
# create a data set  
# choose a leel of tokenization

chars = set()

#read all chars in the dataset

for i in inputs + outputs:
    for ch in i:
        if ch not in chars:
            chars.add(ch)
            
# create input data

max_sent = max([len(x) for x in inputs])
    
#print(len(chars))
print('Max input seq:', max_sent)