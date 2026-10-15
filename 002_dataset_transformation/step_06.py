import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


Apps=["Chat","Video","Study","Games"]
df=pd.read_csv("002_dataset_transformation/day02_usage.csv")

usage=df[Apps].to_numpy()
days=df["Day"].to_numpy()
per_day =usage.sum(axis=1)
shares=usage/per_day[:,None]*100

fig,(ax1,ax2)=plt.subplots(2,1,figsize=(11,8))

for i,app in enumerate(Apps):
    ax1.plot(days,usage[:,i],marker="o",
             markersize=3,linewidth=1.6,label=app)

 

plt.sca(ax1)

plt.title("Daily App Usage")
plt.xlabel("Day")
plt.ylabel("Usage")
plt.legend()
plt.grid(True)

 

 
plt.sca(ax2)

ax2.bar(days, per_day, label="Total Usage")
ax2.bar(days, usage[:, 2], label="Study")

plt.title("Study vs Total Daily Usage")
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.legend()
plt.grid(True)

fig.savefig("002_dataset_transformation/charts")
