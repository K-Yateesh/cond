import random

# ===================================
# 1. Voting Eligibility Check
# ===================================
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# ===================================
# 2. Grade to Letter Conversion
# ===================================
def get_letter_grade(percentage):
    if 90 <= percentage <= 100:
        return "A"
    elif 80 <= percentage < 90:
        return "B"
    elif 70 <= percentage < 80:
        return "C"
    elif 60 <= percentage < 70:
        return "D"
    else:
        return "F"

# Test the function
marks = float(input("\nEnter your percentage: "))
grade = get_letter_grade(marks)
print(f"Your grade is: {grade}")


# ===================================
# 3. Simple Calculator
# ===================================
print("\n--- Simple Calculator ---")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid choice.")


# ===================================
# 4. Random Odd/Even Checker
# ===================================
random_number = random.randint(1, 100)
print("\nGenerated number:", random_number)

if random_number % 2 == 0:
    print("The number is EVEN.")
else:
    print("The number is ODD.")