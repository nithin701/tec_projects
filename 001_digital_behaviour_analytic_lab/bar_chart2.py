import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


df=pd.read_csv("001_digital_behaviour_analytic_lab/digital_behaviour.csv")
instagram_total = df["Instagram_Minutes"].sum()
youtube_total = df["YouTube_Minutes"].sum()
whatsapp_total = df["WhatsApp_Minutes"].sum()
linkedin_total = df["LinkedIn_Minutes"].sum()

 
apps = ["Instagram", "YouTube", "WhatsApp", "LinkedIn"]
totals = [
    instagram_total,
    youtube_total,
    whatsapp_total,
    linkedin_total
] 
 

plt.figure(figsize=(40,20))
plt.bar(apps, totals,color="green") 
 
plt.title("Total_Time_By_App")
plt.xlabel("Apps")
plt.ylabel("minutes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("001_digital_behaviour_analytic_lab/charts/Total_time_by_app")
plt.close()
