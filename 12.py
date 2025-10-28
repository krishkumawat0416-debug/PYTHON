
#ZERO DIVISION ERROR
# a = 10
# b = 2

# this 'try' blocks always runs
# try:
#     c = a/b
#     print(c)
    
# this loop block runs when an exception occurs in the program

# except ZeroDivisionError:
#     print("Error: Division by zero")
    
# this else block runs if no exception occurs

# else:
#     print("c")

# Name error

# try:
#     print(z)
    
# Name error

# except NameError:
#     print("Error: Variable 'z' is not defined")
    
# Type error

# try:
#     a = 'str'
#     b = 10
#     c = a+b
# except TypeError:
#     print("Please use the datat type for this operation")
    
# Value error

# try:
#     a = '23fg32'
#     b = int(a)
# except ValueError:
#     print("Please use the integer value in string typecast")
# else:
#     print(b)

# INDEX ERROR
# li = [1,2,3,4,5]
# try:
#     print(li[6])
# except IndexError:
#     print("Error: Index out of range")
    
# KEY ERROR
# di = {
#     "name": "Arun",
#     "Batch": "A-18",
#     "Mobile No": 9876543210
# }

# try:
#     print(di["name"])   # access using key
# except KeyError:
#     print("Error: Key not found")

# FILE NOT FOUND ERROR
# try:
#     with open('sample.txt','r') as f:
#         content = f.read()
        # print(content)
# This block will run when an exception occurs
# except FileNotFoundError:
#     print("Error: File not found")
# this block will run when any exception occurs
# else:
    # print(content)
# this block will always run
# finally:
#     f.close()
#     print("This block will always run")

# 1. Division with Zero Handling
# Problem: Develop a program that prompts the user for two numbers and performs
# division. Implement exception handling to gracefully manage cases where the user
# attempts to divide by zero.

# a = 100
# b = 50 

# try:
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Division by zero")

# 2. Integer Input Validation
# Problem: Write a program that requests an integer input from the user. Include exception
# handling to catch and manage situations where the user provides a non-integer value.

# try:
#     a = int(input("Enter a number: "))
#     b = int()
# except ValueError:
#     print("Error: Please enter an integer value")
# else:
#     print(b)

    
# 3. File Not Found Handling
# Problem: Create a program designed to open and read the content of a file named
# data.txt. Implement exception handling to specifically address scenarios where
# data.txt does not exist.

# try:
#     with open('data.txt','r') as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("Error: File not found")

# 4. String to Integer Conversion
# Problem: Develop a program that attempts to convert a given string into an integer.
# Include exception handling to manage cases where the string cannot be successfully
# converted to an integer.

# s = input("Enter a number: ")
# try:
#     a = int(s)
#     print(a)
# except ValueError:
#     print("Error: Please enter an integer value")

# 5. List Index Out of Range
# Problem: Write a program that accepts a list of numbers and asks the user for an index.
# Print the element at the user-provided index. Implement exception handling to prevent
# errors if the user enters an index that is outside the valid range of the list.

# ind = int(input("Enter a index: "))
# li = [1,2,3,4,5]
# try:
#     print(li[ind])
# except IndexError:
#     print("Error: Index out of range")
# except ValueError:
#     print("Error: Please enter an integer value")

# 6. Division with Success Message
# Problem: Create a program that takes two numerical inputs and performs a division
# operation. Utilize try...except...else blocks to ensure a success message is printed
# only when the division is completed without any exceptions.

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# try:
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Division by zero")
# else:
#     print("Success: Division completed without errors")

# 7. Custom Negative Number Exception
# Problem: Design a program that prompts the user for a number. If the user enters a
# negative number, raise a custom exception named NegativeNumberError.

# a = int(input("Enter a number: "))
# if a < 0:
#     raise NegativeNumberError
# else:
#     print(a)
# Problem: Write a program that opens a file, reads its content, and guarantees that the file
# is always closed properly, regardless of whether an error occurred during the reading
# process. Use the finally block for this purpose.

# try:
#     with open('sample.txt','r') as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("Error: File not found")
# except Exception as e:
#     print(f"Error: {e}")
    
# finally:
#     try:
#         f.close()
#     except NameError:
#         print("Error: File not opened")
        
# 9. Dictionary Key Not Found
# Problem: Develop a program that asks the user to input a key and then attempts to print
# the corresponding value from a predefined dictionary. Implement exception handling to
# manage situations where the entered key does not exist in the dictionary.

# dic = {
#     "Name" : "Vedang",
#     "Course" : "Python",
#     "Location" : "Jaipur"
# }
# try:
#     user = input("Enter a key: ")
#     print(dic[user])
    
#     value = dic[user]
#     print(value)
    
# except KeyError:
#     print("Error: Key not found")

# 10. Nested Exception Handling
# Problem: Create a program that uses nested try...except blocks. The outer block
# should handle ValueError for invalid input (e.g., non-numeric input for division), and the
# inner block should handle ZeroDivisionError when attempting to divide by zero.

try:
    # Outer try block for invalid input
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))

    try:
        # Inner try block for division
        result = num1 / num2
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numeric values.")

