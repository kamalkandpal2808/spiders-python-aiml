"""Examples of while loops, for loops, and patterns."""

print("Numbers from 1 to 10:")
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1

print("\n\nEven numbers from 1 to 50:")
for number in range(2, 51, 2):
    print(number, end=" ")

print("\n\nSum of first n natural numbers:")
try:
    n = int(input("\nEnter a non-negative integer: "))
    if n < 0:
        print("Please enter zero or a positive integer.")
    else:
        total = sum(range(1, n + 1))
        print(f"Sum of first {n} natural numbers = {total}")
except ValueError:
    print("Please enter a whole number.")

print("\nStar pattern:")
for row in range(1, 6):
    print("*" * row)

print("\nMultiplication table:")
try:
    number = int(input("Enter a number: "))
    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")
except ValueError:
    print("Please enter a whole number.")
