import pandas as pd

def data_generator(column_names):
    data = pd.read_csv("../1617.csv", encoding='latin1')
    data = data[data.X_TOTAL_STUDENTS !=0]
    data['target'] = (data.NO_OF_STUDENTS_PLACED / data.X_TOTAL_STUDENTS ) * 100
    data.target.fillna(0, inplace=True)
    return (data[column_names + ['target']])
