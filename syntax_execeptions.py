# syntax errors occur when the parser detects an incorrect statement
# exceptions are disruptions in running of a program caused by 'Invalid user input', 'File not found', 'ZeroDivision' etc. etc

# using the 'raise' keyword to create custom exceptions when unwanted scenarios are encountered

def divide(x: int, y: int):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y


# when the divide function is used with y = 0, the program halts
# but with the "try-except block" the error is raised and the program continues executing
# the try-except block" can have an else which runs when no errors are found

try:
  test_case = divide(10, 0)
except ZeroDivisionError as a:
    print(f"Error: {a}")
else:
    print(test_case)


# Using the "assert" keyword
# assert is used to check if a condition is met, if not it raises an AssertionError so the raise keyword isn't used


def validate_age(age):
    try:
        assert age >= 18, "You must be at least 18 years old"
        print("You are eligible to vote!")
    except AssertionError as b:
        print(f"Error: {b}")


validate_age(16)

# If the condition is not met, it will print out the error

#try-except-else-finally
# The finally block is executed regardless of exceptions, typically for cleanup.

# try-except-else-finally block example

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        # Handle the case where the divisor is zero
        print("Error: Cannot divide by zero!")
        return None
    else:
        # If no exception occurred, print the result
        print(f"The result is: {result}")
        return result
    finally:
        # This block is executed regardless of whether an exception occurred
        print("Division operation complete.")

#test_case
divide_numbers(10, 2) 
divide_numbers(10, 0)  






