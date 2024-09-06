"""
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
"""
import json

filename = 'person.json'

with open(filename, 'r') as f:
    obj = json.load(f)

print(obj)