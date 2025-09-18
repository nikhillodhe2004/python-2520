# -------------------------------
# Student Grade Tracker Program
# -------------------------------

# Collect Student Information
student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")
attendance = float(input("Enter Attendance Percentage (%): "))

# Collect Scores
scores = []
while True:
    score = float(input("Enter Score/Marks: "))
    scores.append(score)

    another = input("Do you want to enter another score? (yes/no): ").strip().lower()
    if another != "yes":
        break

# Calculate Total, Average, and Count
total_score = sum(scores)
num_scores = len(scores)
average_score = total_score / num_scores if num_scores > 0 else 0

# Determine Grade
if average_score >= 85:
    grade = "A"
elif average_score >= 70:
    grade = "B"
elif average_score >= 50:
    grade = "C"
else:
    grade = "FAIL"

# Attendance Criteria
if attendance < 75:
    attendance_status = "WARNING: LOW ATTENDANCE"
else:
    attendance_status = "OK: GOOD ATTENDANCE"

# Award Eligibility
if attendance >= 75 and grade == "A":
    award = "Eligible for Award 🏆"
else:
    award = "Not Eligible for Award"

# -------------------------------
# Final Output
# -------------------------------
print("\n----- STUDENT REPORT -----")
print(f"Student ID        : {student_id}")
print(f"Student Name      : {student_name}")
print(f"Attendance        : {attendance}%")
print(f"Total Score       : {total_score}")
print(f"Average Score     : {average_score:.2f}")
print(f"Number of Scores  : {num_scores}")
print(f"Student Grade     : {grade}")
print(f"Attendance Status : {attendance_status}")
print(f"Award Eligibility : {award}")
print("--------------------------")
