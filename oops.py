"""Introductory object-oriented programming example."""


class Student:
    """Represent a student with marks and a method to calculate average."""

    def __init__(self, name, branch, marks):
        self.name = name
        self.branch = branch
        self.marks = marks

    def average(self):
        """Return the average of the student's marks."""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}")


if __name__ == "__main__":
    student = Student("kamal", "CSE AI/ML", [90, 85, 92, 99 ])
    student.display()
