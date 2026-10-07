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

 
plt.pie(totals,labels=apps,autopct="%1.1f%%",startangle=90)
plt.title("Share of attention")
plt.savefig("001_digital_behaviour_analytic_lab/charts/Share_of_attention")
plt.show()
plt.close()