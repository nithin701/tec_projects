import csv
import numpy as np

python_scores = []
aptitude_scores = []
communication_scores = []
sql_scores = []

with open("tec_projects\002_project_home_work\placement_readiness.csv", "r", newline="", encoding="utf-8") as f:

    reader = csv.DictReader(f)

    for row in reader:
        python_scores.append(int(row["Python_Score"]))
        aptitude_scores.append(int(row["Aptitude_Score"]))
        communication_scores.append(int(row["Communication_Score"]))
        sql_scores.append(int(row["SQL_Score"]))

scores = np.array(python_scores)
scores_avg = scores.mean()

aptitude = np.array(aptitude_scores)
aptitude_highest = aptitude.max()
aptitude_lowest = aptitude.min()

communication = np.array(communication_scores)
c_greater = communication[communication > 70]

sql = np.array(sql_scores)
skills = np.column_stack((scores, sql, aptitude, communication))
best_score = np.max(skills, axis=1)
worst_score = np.min(skills, axis=1)
skill_gap = best_score - worst_score

print("Average Python Score:", scores_avg)
print("Highest Aptitude Score:", aptitude_highest)
print("Lowest Aptitude Score:", aptitude_lowest)
print("Communication scores above 70:", len(c_greater))
print("The student best score:", best_score)
print("The student worst score:", worst_score)
print("Gap between the best and worst scores:", skill_gap)