 
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
 
df=pd.read_csv("001_digital_behaviour_analytic_lab/digital_behaviour.csv")

df['Total_Screen_Time']=(
    df["Instagram_Minutes"]
    +df["YouTube_Minutes"]
    +df["WhatsApp_Minutes"]
    +df["LinkedIn_Minutes"]
)
df["day_label"]=[f"Day {i+1}" for i in range(len(df))]

plt.figure(figsize=(20,11))
plt.bar(df["day_label"],df["Total_Screen_Time"],color="blue")
plt.title("screen times of the days")
plt.xlabel("days")
plt.ylabel("minutes")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("001_digital_behaviour_analytic_lab/charts/total_screen_time")
plt.close()