import csv
import random

 
NUM_STUDENTS = 50

 
OUTPUT_FILE = "placement_readiness.csv"

 
branches = ["CSE", "ECE", "IT", "MECH"]

 
data = []

for i in range(1, NUM_STUDENTS + 1):
    student = [
        f"S{i:03d}",                          
        random.choice(branches),          
        random.randint(40, 95),               
        random.randint(40, 95),               
        random.randint(35, 95),             
        random.randint(40, 95),             
        random.randint(0, 5),                  
        random.randint(0, 5)                   
    ]

    data.append(student)

 
with open(OUTPUT_FILE, "w", newline="") as file:
    writer = csv.writer(file)

   
    writer.writerow([
        "Student_ID",
        "Branch",
        "Python_Score",
        "SQL_Score",
        "Aptitude_Score",
        "Communication_Score",
        "Projects_Completed",
        "Mock_Interviews_Attended"
    ])

   
    writer.writerows(data)

print(f"{NUM_STUDENTS} student records generated successfully!")
print(f"File created: {OUTPUT_FILE}")