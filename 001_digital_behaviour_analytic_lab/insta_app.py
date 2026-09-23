import csv
import os   
APP ="Instagram"
 

#storing the last 7 days interactions in a list
minutes=[]
with open("001_digital_behaviour_analytic_lab/digital_behaviour.csv", "r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        minutes.append(int(row["Instagram_Minutes"]))
    minutes=minutes[0:7]
    
    
# sum of last 7 days interactions
sum_of_elements=sum(minutes) #775

# average of last 7 days interactions
average=sum_of_elements/len(minutes)

# finding the  maximum in last 7 days interactions
max_interaction=max(minutes)

# finding the minimum in last 7 days interactions
min_interaction=min(minutes)

#finding the above average interactions in last 7 days
counter=0
for i in minutes:
    if i>average:
        counter+=1  
 

#small report of the last 7 days interactions
print(f"Report for :{APP}toatl minutes spent:{sum_of_elements},average minutes spent:{average}, maximum minutes spent:{max_interaction}, minimum minutes spent:{min_interaction}, number of days with above average interactions:{counter}")
 
#