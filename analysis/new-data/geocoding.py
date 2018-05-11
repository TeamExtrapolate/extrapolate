import geocoder
from pymongo import MongoClient
from multiprocessing import Process, Queue

mongo = MongoClient('mongodb://elissa:readability@dhruvkuchhal.com:27017/advice_readability', connect = False)

# mongo = MongoClient('mongodb://localhost:27017', connect = False)
db = mongo['advice_readability']

places = db['aicte_geocoder_results'].distinct('place',{'geocoder_result':None})

def processPlace(process_no):
    ctr = 0
    while(True):
        place = placesQ.get()
        if not db['aicte_geocoder_results'].find_one({'place':place}):
            geocoder_result = geocoder.google(place)
            if geocoder_result:
                db['aicte_geocoder_results'].update({'place':place}, {'$set':{'geocoder_result':geocoder_result.json}}, upsert=True)
            else:
                db['aicte_geocoder_results'].update({'place':place}, {'$set':{'geocoder_result':None}}, upsert=True)
        ctr += 1
        print (str(ctr) + '/' + str(placesQ.qsize()))

placesQ = Queue()

for place in places:
    doc = db['aicte_data'].find_one({'CURRENT_INSTITUTE_ADDRESS':place})
    place = doc['INSTITUTE_DISTRICT'] + ', ' + doc['INSTI_STATE']
    placesQ.put(place)

processes = list()
try:
    for i in range(0, 50):
        processPlaceP = Process(target=processPlace,args=(i,))
        processPlaceP.start()
        processes.append(processPlaceP)
    for process in processes:
        process.join()
except Exception as e:
    raise


# ctr = 0
# total = len(places)
# for place in places:
#     if not db['aicte_geocoder_results'].find_one({'place':place}):
#         geocoder_result = geocoder.google(place)
#         if geocoder_result:
#             db['aicte_geocoder_results'].update({'place':place}, {'$set':{'geocoder_result':geocoder_result.json}}, upsert=True)
#         else:
#             doc = db['aicte_data'].find_one({'CURRENT_INSTITUTE_ADDRESS':place})
#             place = doc['INSTITUTE_DISTRICT'] + ', ' + doc['INSTI_STATE']
#             geocoder_result = geocoder.google(place)
#             if geocoder_result:
#                 db['aicte_geocoder_results'].update({'place':place}, {'$set':{'geocoder_result':geocoder_result.json}}, upsert=True)
#             else:
#                 db['aicte_geocoder_results'].update({'place':place}, {'$set':{'geocoder_result':None}}, upsert=True)
#     ctr += 1
#     print (str(ctr) + '/' + str(total))
