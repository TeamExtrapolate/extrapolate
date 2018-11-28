import numpy as np
import pandas as pd
import random
# import seaborn as sns
# import matplotlib.pyplot as plt
# from scipy.stats import skew
# from sklearn.preprocessing import scale
# import seaborn as sns

data = pd.read_csv("aicte1.csv")

data.head()

data1 = data.copy()

Y = data[['state','number_of_institutes']].groupby('state',as_index=False).sum().sort('number_of_institutes',ascending=False)

print (Y.index.values)
