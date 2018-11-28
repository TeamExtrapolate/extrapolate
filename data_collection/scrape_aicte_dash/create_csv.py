import requests
import json
from pymongo import MongoClient
import csv

client = MongoClient('mongodb://dhruv:Hello123!@localhost/jeevansathi')
db = client['jeevansathi']

collection_aicte_dashboard = db['aicte_dashboard']
fields = ['year', 'institution_type', 'level', 'program', 'state', 'minority', 'women', 'faculties', 'newinstitute', 'closedinstitute', 'institution_count_2012-2016', 'intake_2012-2016', 'enrollment_2012-2016', 'passed_2012-2016', 'placed_2012-2016']
with open('aicte_dashboard.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for doc in collection_aicte_dashboard.find(no_cursor_timeout=True):
        qp = doc['query_params']
        res = doc['result']['records']
        institution_count_12_16 = ""
        for institution_count in res['instituecount']:
            institution_count_12_16 = institution_count_12_16 + str(institution_count) + ", "
        intake_12_16 = ""
        for intake in res['intake']:
            intake_12_16 = intake_12_16 + str(intake) + ", "
        enrollment_12_16 = ""
        for enrollment in res['enrollment']:
            enrollment_12_16 = enrollment_12_16 + str(enrollment) + ", "
        passed_12_16 = ""
        for passed in res['passed']:
            passed_12_16 = passed_12_16 + str(passed) + ", "
        placed_12_16 = ""
        for placed in res['placed']:
            placed_12_16 = placed_12_16 + str(placed) + ", "
        csvwriter.writerow([qp['year'], qp['institutiontype'], qp['level'], qp['program'], qp['state'], qp['Minority'], qp['Women'], res['faculties'], res['newinstitute'], res['closedinstitute'], institution_count_12_16, intake_12_16, enrollment_12_16, passed_12_16, placed_12_16])
#
# import csv
# with open('eggs.csv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     csvwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
