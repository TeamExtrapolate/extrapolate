import requests
# import json
from pymongo import MongoClient
import csv
import simplejson as json
from bson.objectid import ObjectId

class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return obj

client = MongoClient('mongodb://dhruv:Hello123!@localhost/jeevansathi')
db = client['jeevansathi']

fields = ['year', 'institution_type', 'level', 'program', 'state', 'minority', 'women', 'data_colleges']
with open('aicte_database.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    cnt = 0
    total = db.aicte_approved_institutes2.find({"query_params.Minority":{"$ne":None}, "results.aicte_id":{"$ne":None}},no_cursor_timeout=True).count()
    for doc in db.aicte_approved_institutes2.find({"query_params.Minority":{"$ne":None}, "results.aicte_id":{"$ne":None}},no_cursor_timeout=True):
        qp = doc['query_params']
        data_colleges = doc['results']
        for college in data_colleges:
            if 'approved_courses' not in college:
                doc = db.aicte_approved_institutes2_courses.find_one({"aicte_id":college['aicte_id']})
                if doc:
                    college['approved_courses'] = doc
            if 'faculty' not in college:
                doc = db.aicte_approved_institutes2_faculty.find_one({"aicte_id":college['aicte_id']})
                if doc:
                    college['faculty'] = doc

        csvwriter.writerow([qp['year'], qp['institutiontype'], qp['level'], qp['program'], qp['state'], qp['Minority'], qp['Women'], json.dumps(data_colleges, cls=Encoder)])
        cnt = cnt + 1
        print (str(cnt) + "/" + str(total))


    # for doc in collection_aicte_dashboard.find(no_cursor_timeout=True):
    #     qp = doc['query_params']
    #     res = doc['result']['records']
    #     institution_count_12_16 = ""
    #     for institution_count in res['instituecount']:
    #         institution_count_12_16 = institution_count_12_16 + str(institution_count) + ", "
    #     intake_12_16 = ""
    #     for intake in res['intake']:
    #         intake_12_16 = intake_12_16 + str(intake) + ", "
    #     enrollment_12_16 = ""
    #     for enrollment in res['enrollment']:
    #         enrollment_12_16 = enrollment_12_16 + str(enrollment) + ", "
    #     passed_12_16 = ""
    #     for passed in res['passed']:
    #         passed_12_16 = passed_12_16 + str(passed) + ", "
    #     placed_12_16 = ""
    #     for placed in res['placed']:
    #         placed_12_16 = placed_12_16 + str(placed) + ", "
    #     csvwriter.writerow([qp['year'], qp['institutiontype'], qp['level'], qp['program'], qp['state'], qp['Minority'], qp['Women'], res['faculties'], res['newinstitute'], res['closedinstitute'], institution_count_12_16, intake_12_16, enrollment_12_16, passed_12_16, placed_12_16])
#
# import csv
# with open('eggs.csv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     csvwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
