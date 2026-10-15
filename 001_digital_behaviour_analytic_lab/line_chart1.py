import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


df=pd.read_csv("001_digital_behaviour_analytic_lab/digital_behaviour.csv")

df["Total_Screen_Time"] = (
    df["Instagram_Minutes"]
    + df["YouTube_Minutes"]
    + df["WhatsApp_Minutes"]
    + df["LinkedIn_Minutes"]
)

plt.figure(figsize=(40,20))
plt.plot(df["Date"], df["Study_Minutes"], label="Study Minutes")
plt.plot(df["Date"], df["Total_Screen_Time"], label="Total Screen Time")

plt.title("study_VS_total")
plt.xlabel("study")
plt.ylabel("minutes")
plt.legend()
plt.xticks(rotation=45)
plt.savefig("001_digital_behaviour_analytic_lab/charts/Study_VS_total")
plt.close()

plt.sca(ax1)

plt.title("Daily App Usage")
plt.xlabel("Day")
plt.ylabel("Usage")
plt.legend()
plt.grid(True)