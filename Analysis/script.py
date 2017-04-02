import datetime
import pickle

import numpy as np
import pandas as pd


def convertTF(df, featureList):
    d = {True: 1, False: 0}
    for feature in featureList:
        df[feature] = df[feature].apply(lambda x: d[x])
    return df


def yearReturn(x):
    return x.year


def pos(x):
    if x > 0:
        return 1
    else:
        return 0


def neg(x):
    if x < 0:
        return 1
    else:
        return 0


def val(x):
    if x > 0.44:
        return 3
    elif x < -0.44:
        return 1
    else:
        return 2


def conv_english(x):
    if x >= 520:
        return 3
    elif x < 420:
        return 1
    else:
        return 2


def conv_logical(x):
    if x >= 600:
        return 3
    elif x < 450:
        return 1
    else:
        return 2


def conv_quant(x):
    if x >= 600:
        return 3
    elif x < 500:
        return 1
    else:
        return 2


def conv_prog(x):
    if x >= 600:
        return 3
    elif x < 500:
        return 1
    else:
        return 2


def gpaCal(x):
    if x <= 10:
        return x * 10
    else:
        return x


def isNationalBoard(row):
    if (row['isCbse'] or row['isISC'] or row['isICSE']):
        return 1
    else:
        return 0


def prepare(train):
    # Extract Designation
    train['isSenior'] = train.Designation.str.contains('senior')
    train['isSoftware'] = train.Designation.str.contains('software')
    train['isManager'] = train.Designation.str.contains('manager')
    train['isEngineer'] = train.Designation.str.contains('engineer')
    train['isDeveloper'] = train.Designation.str.contains('developer')

    # Extract Degree
    train['isBtech'] = train.Degree.str.contains('B.Tech/B.E.')
    train['isMCA'] = train.Degree.str.contains('MCA')
    train['isMtech'] = train.Degree.str.contains('M.Tech./M.E.')

    # Extract Board of Examination
    train['isCbse'] = train['12board'].str.contains('cbse')
    train['isStateBoard'] = train['12board'].str.contains('state board')
    train['isISC'] = train['12board'].str.contains('isc')
    train['isICSE'] = train['12board'].str.contains('icse')
    train['isCbse'].fillna(value=False, inplace=True)
    train['isStateBoard'].fillna(value=False, inplace=True)
    train['isISC'].fillna(value=False, inplace=True)
    train['isICSE'].fillna(value=False, inplace=True)
    train['isNationalBoard'] = 0
    train['isNationalBoard'] = train.apply(lambda x: isNationalBoard(x), axis=1)

    # Extract Specialization
    train['isCSE'] = train.Specialization.str.contains('computer engineering')
    train['isECE'] = train.Specialization.str.contains('electronics and communication engineering')
    train['isIT'] = train.Specialization.str.contains('information technology')
    train['isMech'] = train.Specialization.str.contains('mechanical engineering')
    train['isICE'] = train.Specialization.str.contains('instrumentation and control engineering')
    train['isEE'] = train.Specialization.str.contains('electrical engineering')

    train = convertTF(train, ['isCbse', 'isStateBoard', 'isISC', 'isICSE', 'isBtech', 'isMCA', 'isMtech', 'isSenior',
                              'isSoftware', 'isManager', 'isEngineer', 'isDeveloper', 'isCSE', 'isECE', 'isIT',
                              'isMech', 'isICE', 'isEE'])

    # Cleaning
    m = train.ComputerProgramming.mean(skipna=True)
    train.ComputerProgramming.fillna(m, inplace=True)

    n = train.Domain.mean(skipna=True)
    train.Domain.fillna(n, inplace=True)

    train.GraduationYear.replace(0, None, inplace=True)
    m = train.GraduationYear.mean(skipna=True)
    train.GraduationYear.fillna(m, inplace=True)

    # Generate Features

    # MaxDomain : max of the domains in one column
    train['maxDomain'] = train[
        ['ComputerProgramming', 'ComputerScience', 'ElectronicsAndSemicon', 'MechanicalEngg', 'ElectricalEngg',
         'TelecomEngg', 'CivilEngg']].max(axis=1)

    # diffGrad : difference between Graduation Year & 12th graduation, to see whether drop in college affect scores
    train['diffGrad'] = train.GraduationYear - train['12graduation']

    # diffGradDOB : difference between Graduation Year and DOB
    train['DOBY'] = train.DOB.apply(yearReturn)
    train['diffGradDOB'] = train.GraduationYear - train.DOBY

    # Big Five scores
    train['bigfive'] = 0
    train.bigfive += train.agreeableness.apply(lambda x: val(x))
    train.bigfive += train.conscientiousness.apply(lambda x: val(x))
    train.bigfive += train.nueroticism.apply(lambda x: val(x))
    train.bigfive += train.extraversion.apply(lambda x: val(x))
    train.bigfive += train.openess_to_experience.apply(lambda x: val(x))

    # Translate English / Logical / Quants scores
    train['scores'] = 0
    train['scores'] += train.English.apply(lambda x: conv_english(x))
    train['scores'] += train.Logical.apply(lambda x: conv_logical(x))
    train['scores'] += train.Quant.apply(lambda x: conv_quant(x))
    train['scores'] += train.ComputerProgramming.apply(lambda x: conv_prog(x))

    # Fix GPA to 100 scale
    train['mcolgGPA'] = train.collegeGPA.apply(lambda x: gpaCal(x))

    # Feature columns to take
    feature_cols = ['10percentage', '12percentage', 'mcolgGPA', 'CollegeTier', 'CollegeCityTier', 'GraduationYear',
                    'scores', 'Domain', 'maxDomain', 'bigfive', 'diffGradDOB', 'isCSE', 'isIT', 'isECE', 'isMech',
                    'isICE', 'isEE']
    X = train[feature_cols]
    y = train.Salary

    return X, y


def testing(X, model, ds, file_name):
    y_pred = np.expm1(model.predict(X))
    submission = pd.DataFrame(columns=['ID', 'Salary'])
    submission.ID = ds.ID
    submission.Salary = y_pred
    Q1 = submission['Salary'].quantile(0.25)
    Q3 = submission['Salary'].quantile(0.75)
    IQR = Q3 - Q1
    threshold_upper = Q3 + 1.5*IQR
    threshold_lower = Q1- 1.5*IQR
    salary_new = pickle.load(open('analysis/salary_std.sav', 'rb'))
    under_employed = submission[submission['Salary'] < int(salary_new.Salary.mean())].shape[0]
    percentage = (under_employed/submission.shape[0])*100
    li = [percentage]
    writer_orig = pd.ExcelWriter(file_name, engine='xlsxwriter')
    submission.to_excel(writer_orig, index=False, sheet_name='report')
    writer_orig.save()
    return li



def execute(file_path):
    test = pd.read_excel(file_path, na_values=-1)
    X, y = prepare(test)
    filename = 'analysis/IKDD_Dataset/finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    path = 'tmp/predictions/result-%s.xlsx' % (int(datetime.datetime.now().strftime("%s")) * 1000)
    data = testing(X, loaded_model, test, path)
    data.append(path)
    return data
