__author__ = 'dhairya'


import pymongo


uri = "mongodb://127.0.0.1:27017/"
client = pymongo.MongoClient(uri)
database = client['test']
collection = database['table1']

# command 1
table1 = collection.find({})
rowlist = []
for rows in table1:
    rowlist.append(rows)
print("Command 1")
print(rowlist)
# Command 2
table2 = [row for row in collection.find({})]
print("Command 2")
print(table2)
print(row for row in collection.find({}))
# Command 3
table3 = [row for row in collection.find({}) if row['mark'] > 80]
print("Command 3")
print(table3)
# Command 4
collection.insert({'mark': 70, 'name': 'Dash'}) # insert the data in the table1
# Command 5
table4 = collection.find_one({'mark': 70})
print("Command 5 ")
print(table4)
