"""Basic examples of list, tuple, set, and dictionary."""

# List: ordered and mutable
marks = [88, 75, 89, 85]
marks.append(81)
print("List:", marks)
print("First mark:", marks[0])

# Tuple: ordered and immutable
point = (10, 20)
print("\nTuple:", point)

# Set: stores unique values
unique_marks = set(marks)
print("\nUnique marks:", unique_marks)

# Dictionary: key-value pairs
student = {"name": "kamal", "branch": "CSE AI/ML", "semester": 5}
student["semester"] = 6
print("\nDictionary:", student)
print("Student name:", student["name"])

print("\nLoop through dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")
