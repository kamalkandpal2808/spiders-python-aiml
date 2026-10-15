"""Conditional statements: if, elif, and else."""

try:
    marks = float(input("Enter marks from 0 to 100: "))
except ValueError:
    print("Please enter a valid number.")
else:
    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 40:
        print("Grade: D")
    else:
        print("Grade: F")
