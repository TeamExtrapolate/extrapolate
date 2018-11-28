import numpy as np
import pandas as pd
# import random
# from scipy.stats import skew
# from scipy.stats import boxcox
# from sklearn.preprocessing import scale

data = pd.read_csv("aicte_dashboard.csv")

data = data.ix[data.faculties < 20000]

data.drop(data[data.faculties == 0].index, inplace = True)

data.faculties.dropna(inplace=True)

data.drop(['year','closedinstitute', 'newinstitute'], axis = 1, inplace = True)

def convertTF(df,featureList):
    d = {'Y':1, '1':0}
    for feature in featureList:
        df[feature] = df[feature].apply(lambda x: d[x])
    return df

train = convertTF(data, ['minority', 'women'])

train.rename(columns= {'institution_count_2012-2016': 'number_of_institutes',
                      'intake_2012-2016': 'intake',
                      'enrollment_2012-2016': 'enrollment',
                      'passed_2012-2016': 'passed',
                      'placed_2012-2016': 'placed'}, inplace = True)

X = train.copy()

import numbers
def mapped(x):
    if isinstance(x,numbers.Number):
        return x
    for tpe in (int, float):
        try:
            return tpe(x)
        except ValueError:
            continue
    return 0

for i in range(train.shape[0]):
    print (i)
    a = train['intake'].iloc[[i]].str.split(', ').max()
    a = a[:5]
    a = map(mapped,a)
    train['intake'].iloc[[i]] = max(a)

for i in range(train.shape[0]):
    print (i)
    a = train['number_of_institutes'].iloc[[i]].str.split(', ').max()
    a = a[:5]
    a = map(mapped,a)
    train['number_of_institutes'].iloc[[i]] = max(a)

for i in range(train.shape[0]):
    print (i)
    a = train['placed'].iloc[[i]].str.split(', ').max()
    a = a[:5]
    a = map(mapped,a)
    train['placed'].iloc[[i]] = max(a)

for i in range(train.shape[0]):
    print (i)
    a = train['passed'].iloc[[i]].str.split(', ').max()
    a = a[:5]
    a = map(mapped,a)
    train['passed'].iloc[[i]] = max(a)

for i in range(train.shape[0]):
    print (i)
    a = train['enrollment'].iloc[[i]].str.split(', ').max()
    a = a[:5]
    a = map(mapped,a)
    train['enrollment'].iloc[[i]] = max(a)

train.to_csv("data.csv", index=False)
