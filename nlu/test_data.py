import yaml
import os
import json

data = yaml.safe_load(open('nlu\\train.yaml').read())

for command in data['commands']:
    print(command)