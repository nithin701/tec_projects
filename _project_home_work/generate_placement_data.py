
import csv
import os
import random
 
NUM_STUDENTS = 50

OUTPUT_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "placement_readiness.csv"
)

 
random.seed()

COLUMNS = [
    "Student_ID",
    "Branch",
    "Python_Score",
    "SQL_Score",
    "Aptitude_Score",
    "Communication_Score",
    "Projects_Completed",
    "Mock_Interviews_Attended",
]

 
def make_one_student(student_number):
    """Create one simulated student's placement readiness data."""

    student_id = f"STU{student_number:03d}"

    branch = random.choice([
        "CSE",
        "ECE",
        "IT",
        "MECH"
    ])
 
    python_score = random.randint(20, 99)
    sql_score = random.randint(20, 99)
    aptitude_score = random.randint(20, 99)
    communication_score = random.randint(20, 99)

  
    projects_completed = random.randint(0, 6)
    mock_interviews_attended = random.randint(0, 5)

    return [
        student_id,
        branch,
        python_score,
        sql_score,
        aptitude_score,
        communication_score,
        projects_completed,
        mock_interviews_attended,
    ]

 
def build_rows(num_students):
    rows = []

    for student_number in range(1, num_students + 1):
        student = make_one_student(student_number)
        rows.append(student)

    return rows

 
def write_csv(filename, columns, rows):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
 
        writer.writerow(columns)
 
        writer.writerows(rows)

 

def main():
    rows = build_rows(NUM_STUDENTS)

    write_csv(
        OUTPUT_FILE,
        COLUMNS,
        rows
    )

    print(f"{OUTPUT_FILE} created successfully!")
    print(f"Rows: {len(rows)}")
    print(f"Columns: {len(COLUMNS)}")
    print()
    print("Generated placement_readiness.csv successfully.")
    print("You can now open the file in Excel.")


if __name__ == "__main__":
    main()

