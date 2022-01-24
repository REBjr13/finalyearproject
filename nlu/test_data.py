import yaml
import os
import json


data = yaml.safe_load(open('train.yaml'))

for command in data['commands']:
    print(command)