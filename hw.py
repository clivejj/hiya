'''
name: Pokedex
desc: has info about every pokemon from the 1st game
link: https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
imported using json.load and accessing the first element, which is the list of every pokemon's dictionary
'''

import json
import pymongo as p
from pprint import pprint

connection = p.MongoClient('homer.stuy.edu')
db = connection['abedinM-johnstonC']
c = db['pokedex']

#data = json.load(open('pokedex.json'))['pokemon']

#for record in data:
#    c.insert(record)

def types(t):
    for each in c.find({'type' : t}):
        pprint(each)

def ids(lo, hi):
    for each in c.find({'id' : {'$gte' : lo, '$lte' : hi}}):
        pprint(each)

def idType(lo, hi, t):
    for each in c.find({'type' : t, 'id' : {'$gte' : lo, '$lte' : hi}}):
        pprint(each)

def idSpawn(lo, hi, s):
    for each in c.find({'spawn_chance' : {'$lte' : s}, 'id' : {'$gte' : lo, '$lte' : hi}}):
        pprint(each)
        
#finds pokemon with at least 4 weaknesses
def clever():
    for each in c.find({'weaknesses.3' : {'$exists' : 'true'}}):
        pprint(each)

#types('Dragon')
#ids(0,5)
#idType(0, 50, "Flying")
#idSpawn(0, 50, 0.1)
#clever()
