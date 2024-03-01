import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df=pd.read_csv('SSQ_0126.csv')
list=[df.iloc[:,i:i+1] for i in range(df.shape[1])]

print(list)
for i in range(df.shape[1]//2):
    t_statistic, p_value = stats.ttest_rel(list[2*i], list[2*i+1])
    print("ｔ値：",t_statistic, "p値：",p_value/2)

