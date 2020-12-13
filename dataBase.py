
from flask import json


def setCountry(country):
    dict = {'country': country,}
    with open('country.json', 'w') as f:
        json.dump(dict, f)
        
def setCategory(category):
    dict = {'category': category,}
    with open('category.json', 'w') as f:
        json.dump(dict, f)

def getCountry():
    with open('country.json', 'r') as f:
        data = json.load(f)
        country = data['country']
        return country

def getCategory():
    with open('category.json', 'r') as f:
        data = json.load(f)
        category = data['category']
        return category