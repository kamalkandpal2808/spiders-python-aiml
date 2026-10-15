

name = "kamal"          # str
age = 22                # int
height = 1.67           # float (metres)
is_student = True        # bool
subjects = ["Python", "DSA", "AI/ML"]  # list
coordinates = (30.3, 78.0)              # tuple
skills = {"Python", "Git"}              # set
student = {"name": name, "age": age}    # dict

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)
print("Subjects:", subjects)
print("Coordinates:", coordinates)
print("Skills:", skills)
print("Student dictionary:", student)

print("\nData types:")
for label, value in [
    ("name", name),
    ("age", age),
    ("height", height),
    ("is_student", is_student),
    ("subjects", subjects),
    ("coordinates", coordinates),
    ("skills", skills),
    ("student", student),
]:
    print(f"{label}: {type(value).__name__}")
