#///// super calculator \\\\

import numpy as np
import csv

insta_minutes =[]
study_minutes =[]

with open("001_digital_behaviour_analytic_lab/digital_behaviour.csv", "r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        insta_minutes.append(int(row["Instagram_Minutes"]))
        study_minutes.append(int(row["Study_Minutes"]))
        
insta_minutes=insta_minutes[:7]
study_minutes=study_minutes[:7]

instagram=np.array(insta_minutes)
study=np.array(study_minutes)

print("Insta array followed by study array : ",instagram,study)

#total=np.sum(instagram) // it is the standard form ,while using this v may loss the some objects
insta_total=instagram.sum()
insta_average=instagram.mean()
insta_maximum=instagram.max()
insta_minimum=instagram.min()
insta_days=len(instagram)

study_total=study.sum()
study_average=study.mean()
study_maximum=study.max()
study_minimum=study.min()
study_days=len(study)

print(f"insta info (Total :{insta_total},Average :{insta_average}, Maximum :{insta_maximum},Minimum :{insta_minimum},Days :{insta_days})")
print(f"study info (Total :{study_total},Average :{study_average}, Maximum :{study_maximum},Minimum :{study_minimum},Days :{study_days})")

print("Indexed val in instagram : ",instagram[0], instagram[-1], instagram[2])

print("Slicing on instagram : ",instagram[0:3], instagram[-2:], instagram[1:5], instagram[::2])

insta_hours = instagram /60

#insta_hours = np.round(insta_hours,2)  standard form
insta_hours=insta_hours.round(2)
print("Insta_hours : ",insta_hours)

difference =study - instagram
# in simple python it will perform set operation ex[100,200,300,400]-[10,20,30,400],ans=400 only
#in numpy the ans is [90,180,270,0]
print("Difference b/w study & instagram : " ,difference)

#greater =[val for val in difference if val >100] # list comprehenstion
#///same operation using the numpy\\\
greater = instagram > 100
print("Greater insta value than 100 : ",greater)

#filtering the above for only yes
#using python = greater =[bool_ for bool_ in boolean if bool_]
#greater =filter(lamda bool_ : bool_,boolean)//lamda function
#////now using the numpy \\\\\
#greater = instagram[boolean] // will also work
greater =instagram[instagram > 100]

"""count =(instagram >100)
count =count.sum()
# will be done in single line"""
count =(instagram >100).sum()


value = instagram[instagram > insta_average]
