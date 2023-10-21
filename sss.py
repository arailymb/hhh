#task 1 
name = input("Enter your name please: ")
salary = input("Enter your desired salary level: ")

try:
    salary = int(salary)
    tax_level = salary * 0.2
    print(f"{name}, the tax level you will pay with the salary {salary} is {tax_level}")
except ValueError:
    print(f"{name}, please enter your desired salary as a digit.")

#task 2
operation = int(input("Please choose the task you want to perform:\n1. Addition\n2. Multiplication\n3. Division\n4. Exponentiation\n"))

if operation == 1:
    numbers = input("Please enter two numbers for addition, comma separated: ").split(",")
    result = lambda x, y: int(x) + int(y)
    print(result(numbers[0], numbers[1]))
elif operation == 2:
    numbers = input("Please enter two numbers for multiplication, comma separated: ").split(",")
    result = lambda x, y: int(x) * int(y)
    print(result(numbers[0], numbers[1]))
elif operation == 3:
    numbers = input("Please enter two numbers for division, comma separated: ").split(",")
    result = lambda x, y: int(x) / int(y)
    print(result(numbers[0], numbers[1]))
elif operation == 4:
    numbers = input("Please enter two numbers for exponentiation, comma separated: ").split(",")
    result = lambda x, y: int(x) ** int(y)
    print(result(numbers[0], numbers[1]))
else:
    print("Invalid choice")

#task 3
length = int(input("Please enter the length of Fibonacci sequence: "))

fibonacci_sequence = [1, 1]

if length == 1:
    print(f"The Fibonacci sequence for {length} is {fibonacci_sequence[0]}")
elif length == 2:
    print(f"The Fibonacci sequence for {length} is {', '.join(map(str, fibonacci_sequence))}")
else:
    for i in range(2, length):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
    print(f"The Fibonacci sequence for {length} is {', '.join(map(str, fibonacci_sequence))}")

#task 4
input = input("Please chose the task you want to perform:\n 1. Enter items\n2. Exit")
