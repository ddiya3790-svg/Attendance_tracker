# ==========================================================
# Name: Diya Das
# Date: 12-Nov-2025
# Assignment Title: Assignment 01 - Attendance Tracker
# Course: MCA (AI & ML)
# ==========================================================

# Importing required module for bonus task
from datetime import datetime

# -----------------------------
# Task 1: Setup & Introduction
# -----------------------------
print("="*50)
print("WELCOME TO THE PYTHON ATTENDANCE TRACKER TOOL")
print("="*50)
print("This tool helps record and manage attendance easily.")
print("It collects student names with check-in times, validates inputs,")
print("and displays a clean attendance summary.\n")

# -----------------------------
# Task 2: Input & Data Collection
# -----------------------------
attendance = {} 

try:
    n = int(input("Enter the number of attendance entries you want to record: "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
    n = 0

for i in range(n):
    print(f"\n--- Entry {i+1} ---")
    while True:
        name = input("Enter student name: ").strip()

        # Task 3: Data Validation
        if name == "":
            print("Name cannot be empty. Please re-enter.")
            continue
        if name in attendance:
            print("Duplicate entry! This student is already marked present.")
            continue

        time = input("Enter check-in time (e.g., 09:15 AM): ").strip()
        if time == "":
            print("Check-in time cannot be empty. Please re-enter.")
            continue

    
        attendance[name] = time
        print("Record added successfully.")
        break

# -----------------------------
# Task 4: Attendance Summary Generation
# -----------------------------
print("\n\nATTENDANCE SUMMARY".center(50, "-"))
print(f"{'Student Name':<25}{'Check-in Time':<15}")
print("-"*45)

for name, time in attendance.items():
    print(f"{name:<25}{time:<15}")

print("-"*45)
print(f"Total Students Present: {len(attendance)}")

# -----------------------------
# Task 5: Absentee Validation (Optional)
# -----------------------------
try:
    total_students = int(input("\nEnter total number of students in class (for absentee check): "))
    absentees = total_students - len(attendance)
    if absentees < 0:
        absentees = 0
    print(f"Total Present: {len(attendance)}")
    print(f"Total Absent: {absentees}")
except ValueError:
    print("Skipped absentee check (invalid input).")

# -----------------------------
# Task 6: Save Attendance Report to File (Bonus)
# -----------------------------
save_choice = input("\nDo you want to save the attendance record to a file? (yes/no): ").lower()

if save_choice == "yes":
    try:
        with open("attendance_log.txt", "w") as file:
            file.write("ATTENDANCE LOG\n")
            file.write("="*40 + "\n")
            file.write(f"{'Student Name':<25}{'Check-in Time':<15}\n")
            file.write("-"*40 + "\n")
            for name, time in attendance.items():
                file.write(f"{name:<25}{time:<15}\n")
            file.write("-"*40 + "\n")
            file.write(f"Total Present: {len(attendance)}\n")

            if 'total_students' in locals():
                file.write(f"Total Absent: {absentees}\n")

            file.write(f"Report Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        print("Attendance successfully saved to 'attendance_log.txt'")
    except Exception as e:
        print(f"Error while saving file: {e}")
else:
    print("Record not saved.")

print("\nThank you for using the Python Attendance Tracker!")
print("="*50)
