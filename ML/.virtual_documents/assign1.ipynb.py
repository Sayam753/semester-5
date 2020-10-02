import numpy as np
import pandas as pd


df = pd.read_csv("train.csv")


df.head()


df.groupby(["4"]).agg(['mean', 'count'])


for i in df.groupby(["4"]):
    print(type(i), i[1], len)



