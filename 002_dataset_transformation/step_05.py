import pandas as pd
import numpy as np
#A
df=pd.read_csv("day02_usage.csv")
apps=["Chat","Video","Study","Games"]
data=df[apps].to_numpy()
print(data.shape)
#B
print(f"sum of cols: {data.sum(axis=0)}")
print(f"sum of rows: {data.sum(axis=1)}")
print(f"mean of cols: {data.mean(axis=0)}")
print(f"mean of rows: {data.mean(axis=1)}")
print(f"max of cols: {data.max(axis=0)}")
print(f"max of rows: {data.max(axis=1)}")
print(f"min of cols: {data.min(axis=0)}")
print(f"min of rows: {data.min(axis=1)}")
#C
names=np.array(apps)
pos=np.array(data.argmax(axis=1))
winners=names[pos]
#names is a list and pos is a list, here we access pos value as index to names values.
print(f"Winners of each day: {winners}")
values,count=np.unique(winners,return_counts=True)
print(dict(zip(values,count)))
#D
per_day=data.sum(axis=1)
shares=data/per_day[:,None]*100
print(shares.sum(axis=1))
#print(per_day.shape) ==> (30,)
#print(per_day[:,None].shape) ==> (30,1)
#print(np.round(shares.mean(axis=0),1))
app_max=data.max(axis=0)
scale=data/app_max
print(scale)
#E
weekend_mask=(df['Day']%6==0) | (df['Day']%7==0)
print(np.round(data[weekend_mask].mean(axis=0),1))
print(per_day.argmax(),per_day.max())