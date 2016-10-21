import pymongo
import datetime
import sys

connection = pymongo.MongoClient("mongodb://localhost")
db=connection.students
scores = db.grades

def find():

    print "find, reporting for duty"

    query = {'type': 'homework'}
    projection = {'student_id': 1, 'score':1, 'type':1 ,'_id':1}
    sort = { 'student_id':1 , 'score':1}
#    projection = {'student_id': 1}

    try:
        cursor = scores.find(query, projection)
        cursor.sort([('student_id', pymongo.ASCENDING),
                     ('score', pymongo.ASCENDING)])

    except Exception as e:
        print "Unexpected error:", type(e), e

    sanity = 0
    for doc in cursor:

    	if ( sanity == doc['student_id']):
    			remove_student(doc['_id'])
    			sanity += 1


    	#if (sanity == cid):
       	#print doc
def remove_student(id):

    # get a handle to the school database
    try:

        result = scores.delete_one({'_id':id})
       

    except Exception as e:
        print "Exception: ", type(e), e    
        


if __name__ == '__main__':
    find()