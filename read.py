data = open('movies.json').read()
import json
print data.json()

import pymongo as p
connection = p.MongoClient('homer.stuy.edu')
db = connection['hiya']
collection = db['movies']

