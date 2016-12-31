__author__ = "Arjun"

import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

AllStudents = collection.find({})
students_list = []

for students in AllStudents:
    if students['score'] == 99:
        students_list.append(students['score'])

#in one line

students1 = [temp['score'] for temp in collection.find({}) if temp['score'] == 99]

print students_list
print students1