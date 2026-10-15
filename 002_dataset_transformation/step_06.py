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

fig.savefig("002_dataset_transformation/charts")

