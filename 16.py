# Hybrid Inheritance
# class father:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# class child(father):
#     def __init__(self,name,age):
#         super().__init__(name,age)
        # # decorator
        # self.name = name
        # self.age = age
        # # generater
        # #iterator
        # self.name = name
        # self.age = age
        
# Decorator -> a function that takes another function as an argument and returns a new function with enhanced functionality

# def my_decorator(display):  # this task will run before the main function runs
#     def wrapper(): -> to relate
#         print("this task will run before the main function runs")
#         display()
#         print("this task will run after the main function runs")
#     return wrapper

# @my_decorator
# def display():
#     print("This is another task")
#     print("This is the display function")
# display()

# def decorater(func):
#     def wrapper(a,b):
#         print("This task will run before the main function does")
#         a = a+b
#         func(a,b)
        
#         print("This is the task which will run after the main function")
#     return wrapper

# @decorater
# def multiply(a,b):
#     print(a*b)
# def addition(a,b):
#     print(a+b)
# multiply(2,6)
# addition (2,6)

# you are making a banking application everytime someone performance transaction (deposit and withdraw) unique to log the date ,time and name
# before performing the operation

# def log(func):
#     def wrapper(username,amount):
#         print(f"user name:{username}")  
#         print(f"the transaction time{date.datetime.now()}")
#         func(username,amount)
#         print("Transaction completed")

# @log
# def deposit(username,amount):
#     print(f"Deposited {amount} into {username}'s account")
# @log
# def withdraw(username,amount):
#     print(f"Withdrew {amount} from {username}'s account")

# withdraw("vedant",500)
        
# write a decoretor check positive that ensures all the arguments passed to a funcation are positive integers 
# if any negative print only postive allowed

def pos(func):
    def wrapper(a,b):
        print(f"The postive number{a,b}")
        func(a,b)
        print("The postive number are only allowed")
    return wrapper
@pos
def positive(a,b):
    if a>0 and b>0:
        print(a,b)
    else:
        print("Only positive number are allowed")

positive(3,-8)
# print(a,b)