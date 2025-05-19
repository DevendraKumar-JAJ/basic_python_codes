import sys
print('Name '*3)
# print name 3 times...

def mul(name,times=1):
  return name*times

print(mul('Dev ',5))

thislist = ["apple", 25,True,4j]
[print (type(x)) for x in thislist] # printing type of all list  mambers 


# # Python Code Snippets 🐍

# A collection of Python code snippets demonstrating various concepts. 🤔

# # Snippet 1: Printing a String Multiple Times 📝
# - Prints the string 'Name ' three times using the * operator.
# - Output: Name Name Name

# # Snippet 2: Multiplying a String 🔁
# - Defines a function mul that takes a string name and an integer times as arguments.
# - Returns the string name repeated times number of times.
# - Output: Dev Dev Dev Dev Dev

# # Snippet 3: Printing Types of List Members 📚
# - Creates a list thislist containing different data types (string, integer, boolean, complex number).
# - Uses a list comprehension to print the type of each list member.
# # - Output:
#     - <class 'str'>
#     - <class 'int'>
#     - <class 'bool'>
#     - <class 'complex'>