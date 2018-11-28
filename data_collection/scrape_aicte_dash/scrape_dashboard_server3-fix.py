import requests
import json
from pymongo import MongoClient
from multiprocessing import Process, Queue

def sendmail(subject, message):
    return requests.post(
    "https://api.mailgun.net/v3/sandboxa117dd2f574e4f91a2feda15730c6c19.mailgun.org/messages",
    auth=("api", "key-5c8f81281891a6497d2985c23d3b3d27"),
    data={"from": "Data Collection - AICTE Dashboard <mailgun@sandboxa117dd2f574e4f91a2feda15730c6c19.mailgun.org>",
          "to": ["dhruvkuchhal96@gmail.com"],
          "subject": subject,
          "text": message})

client = MongoClient('mongodb://dhruv:Hello123!@dhruvkuchhal.com/jeevansathi')
db = client['jeevansathi']

collection_aicte_dashboard = db['aicte_dashboard']

years = [0,1,2,3,4]
programs = ['ENGINEERING AND TECHNOLOGY', 'APPLIED ARTS AND CRAFTS','ARCHITECTURE AND TOWN PLANNING','HOTEL MANAGEMENT AND CATERING','MANAGEMENT','MCA','PHARMACY']
levels = ['UG','PG','DIPLOMA']
inst_types = ['Unaided - Private','Central University','Deemed University(Government)','Deemed University(Private)','Government','Govt aided','Private-Aided','University Managed-Govt ', 'University Managed-Private ']
states = ['Andaman and Nicobar Islands','Andhra Pradesh ','Arunachal Pradesh ','Assam','Bihar','Chandigarh','Chhattisgarh', 'Dadra and Nagar Haveli','Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Orissa','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
minorities = ['1','Y']
women = ['1','Y']

def getData(method, params):
    query = "http://www.aicte-india.org/" + method
    for param_name in params:
        query = query + "&" + param_name + "=" + params[param_name]
    print ("\n")
    print (query)
    print ("\n")
    return json.loads(requests.get(query).text)

def getParams():
    for doc in db.aicte_dashboard.find({"query_params.institutiontype":"University Managed"}):
        cnt = 0
        params = doc['query_params']
        for inst_type in ['University Managed-Govt ', 'University Managed-Private ']:
            params['institutiontype'] = inst_type
            cnt = cnt + 1
            if not collection_aicte_dashboard.find_one({"query_params":params}):
                paramsQ.put(params)
            else:
                print ("Already processed. cnt = " + str(cnt))
        # db.aicte_dashboard.remove({"query_params":doc['query_params']})
        # print ("REMOVED " + str(doc['query_params']) + "\n")

def processParams(process_no):
    try:
        while(True):
            while(paramsQ.qsize() > 0):
                params = paramsQ.get()
                result = getData("dashboard/pages/php/dashboardserver.php?", params)
                doc = {}
                doc['query_params'] = params
                doc['result'] = result
                collection_aicte_dashboard.update({"query_params" : params}, doc, upsert = True)
                print ("[" + str(process_no) + "] " + "INSERTED : " + str(result))
    except Exception as e:
        cout(sendmail("Exception occurred!", str(e)))
    raise

paramsQ = Queue()

paramsP = Process(target=getParams)
paramsP.start()
while(True):
    if(paramsQ.qsize() > 5):
        # processParamsP = Process(target=processParams,args=(1,))
        # processParamsP.start()
        # break
        for i in range(0, 20):
            processParamsP = Process(target=processParams,args=(i,))
            processParamsP.start()
        break
