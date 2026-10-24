# Python Foundations — Practice Workbook

Small exercises for a beginner using Python. Type each example yourself, run it, then change it and observe what happens.

## 1. Print a message

```python
print("Hello, world!")
print("I am learning Python one step at a time.")
```

**Try it:** Change the messages and run the file again.

## 2. Variables

```python
name = "Marsh"
learning_days = 90

print(name)
print(learning_days)
```

A variable gives a value a name. Strings hold text; integers hold whole numbers.

**Try it:** Create a variable for a skill you want to learn and print it.

## 3. User input

```python
name = input("What is your name? ")
print("Welcome, " + name + "!")
```

**Try it:** Ask the user which programming topic they are practising.

## 4. Numbers and conversion

```python
age_text = input("Enter your age: ")
age = int(age_text)
print("Next year you will be", age + 1)
```

`input()` returns text. `int()` converts numeric text to an integer; invalid input raises an error.

**Try it:** Ask for two numbers and print their sum.

## 5. Conditions

```python
score = int(input("Enter a score from 0 to 100: "))

if score >= 50:
    print("Pass")
else:
    print("Keep practising")
```

Python uses indentation to show which statements belong to a condition.

**Try it:** Add an `elif` branch for a score below 0 or above 100.

## 6. Loops

```python
for number in range(1, 6):
    print(number)
```

This prints the numbers 1 through 5. The stop value in `range()` is not included.

**Try it:** Print the numbers from 1 to 10 and their squares.

## 7. Functions

```python
def greet(name):
    return "Hello, " + name + "!"

message = greet("Marsh")
print(message)
```

A function packages reusable logic. Parameters provide input; `return` sends a result back.

**Try it:** Write an `add(a, b)` function that returns the sum.

## 8. Lists

```python
topics = ["variables", "conditions", "loops"]
topics.append("functions")

for topic in topics:
    print(topic)
```

A list stores an ordered collection of items.

**Try it:** Make a list of three project ideas and print each one.

## 9. Mini-project — Simple calculator

Create a file named `calculator.py`. Ask for two numbers and an operation (`+`, `-`, `*`, or `/`). Use conditions to calculate the result. Check for division by zero and give a clear message for an unknown operation.

## Good practice

- Use meaningful variable names.
- Keep indentation consistent.
- Read the complete error message.
- Test normal input and unexpected input.
- Avoid copying code without understanding it.
- When stuck, isolate the smallest example that reproduces the problem.
