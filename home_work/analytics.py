import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("home_work/placement_readiness.csv")

python = df["Python_Score"].to_numpy()
sql = df["SQL_Score"].to_numpy()
aptitude = df["Aptitude_Score"].to_numpy()
communication = df["Communication_Score"].to_numpy()
 
print("Average Python score:", np.mean(python))
 
print("Highest Aptitude score:", np.max(aptitude))
print("Lowest Aptitude score:", np.min(aptitude))
 
print("Students above 70 in Communication:", np.sum(communication > 70))
 
scores = np.column_stack((python, sql, aptitude, communication))

best = np.max(scores, axis=1)
worst = np.min(scores, axis=1)

gap = best - worst

print("Gap for every student:", gap)

#part 2
#using pandas
 


# 1. Inspect the data

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDescription:")
print(df.describe())


# 2. Show only students with Python above 75

python_above_75 = df[df["Python_Score"] > 75]

print("\nStudents with Python score above 75:")
print(python_above_75)


# 3. Sort the table by Aptitude, highest first

sorted_aptitude = df.sort_values(
    by="Aptitude_Score",
    ascending=False
)

print("\nStudents sorted by Aptitude:")
print(sorted_aptitude)


# 4. Show the top 10 students by Python score

top_10_python = df.sort_values(
    by="Python_Score",
    ascending=False
).head(10)

print("\nTop 10 students by Python score:")
print(top_10_python)


# 5. Students strong in Python but weak in Communication

strong_python_weak_communication = df[
    (df["Python_Score"] > 75) &
    (df["Communication_Score"] < 60)
]

print("\nStudents strong in Python but weak in Communication:")
print(strong_python_weak_communication)

#part 3
# Total score of four skills
df["Total_Score"] = (
    df["Python_Score"]
    + df["SQL_Score"]
    + df["Aptitude_Score"]
    + df["Communication_Score"]
)

# Average score
df["Average_Score"] = df["Total_Score"] / 4

# Weakest skill score
df["Weakest_Skill_Score"] = df[
    ["Python_Score", "SQL_Score", "Aptitude_Score", "Communication_Score"]
].min(axis=1)

# Readiness score
df["Readiness_Score"] = (
    df["Average_Score"]
    + (2 * df["Projects_Completed"])
    + df["Mock_Interviews_Attended"]
)

# Cap Readiness Score at 100
df["Readiness_Score"] = df["Readiness_Score"].clip(upper=100)

print(df.head())

#part 4
def classify_readiness(score):
    if score >= 75:
        return "Ready"
    elif score >= 60:
        return "Almost Ready"
    else:
        return "Needs Work"


df["Readiness_Band"] = df["Readiness_Score"].apply(classify_readiness)

print(df[[
    "Student_ID",
    "Readiness_Score",
    "Readiness_Band"
]])

band_counts = df["Readiness_Band"].value_counts()

print("\nStudents in each band:")
print(band_counts)

largest_band = band_counts.idxmax()

print("\nLargest band:", largest_band)

#part  5
skill_averages = [
    df["Python_Score"].mean(),
    df["SQL_Score"].mean(),
    df["Aptitude_Score"].mean(),
    df["Communication_Score"].mean()
]

skills = [
    "Python",
    "SQL",
    "Aptitude",
    "Communication"
]

plt.figure(figsize=(8, 5))

plt.bar(skills, skill_averages)

plt.title("Average Score for Each Skill")
plt.xlabel("Skill")
plt.ylabel("Average Score")
plt.savefig("home_work/charts/Graphs")

plt.show()

# Chart 2 — Readiness bands

plt.figure(figsize=(8, 5))
plt.bar(band_counts.index, band_counts.values)

plt.title("Students in Each Readiness Band")
plt.xlabel("Readiness Band")
plt.ylabel("Number of Students")
plt.savefig("home_work/charts/Graphs2")

plt.show()


# Chart 3 — Average readiness by branch

branch_readiness = df.groupby("Branch")["Readiness_Score"].mean()

plt.figure(figsize=(8, 5))
plt.bar(branch_readiness.index, branch_readiness.values)

plt.title("Average Readiness Score by Branch")
plt.xlabel("Branch")
plt.ylabel("Average Readiness Score")
plt.savefig("home_work/charts/Graphs3")

plt.show()