 
import csv
 
python_scores = []
sql_scores = []
aptitude_scores = []
communication_scores = []

with open("002_project_home_work/placement_readiness.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        python_scores.append(int(row["Python_Score"]))
        sql_scores.append(int(row["SQL_Score"]))
        aptitude_scores.append(int(row["Aptitude_Score"]))
        communication_scores.append(int(row["Communication_Score"]))


 
# 1. AVERAGE PYTHON SCORE
 

average_python = sum(python_scores) / len(python_scores)

print("1. Average Python Score:", average_python)


 
# 2. HIGHEST AND LOWEST APTITUDE SCORE
 

highest_aptitude = max(aptitude_scores)
lowest_aptitude = min(aptitude_scores)

print("2. Highest Aptitude Score:", highest_aptitude)
print("   Lowest Aptitude Score:", lowest_aptitude)

 
# 3. STUDENTS ABOVE 70 IN COMMUNICATION
 
above_70 = 0

for score in communication_scores:
    if score > 70:
        above_70 += 1

print("3. Students scoring above 70 in Communication:", above_70)

 
# 4. GAP BETWEEN BEST AND WORST SKILL
 

print("4. Gap between best and worst skill for every student:")

for i in range(len(python_scores)):

    student_skills = [
        python_scores[i],
        sql_scores[i],
        aptitude_scores[i],
        communication_scores[i]
    ]

    best_skill = max(student_skills)
    worst_skill = min(student_skills)

    gap = best_skill - worst_skill
 
    print("Student", i + 1, "-> Gap:", gap)
 
