
# Function is used to remove redented code..
def sum(a,b):
  return a+b

# print(sum(9,9))
# def is keyword in py which is used to define a function...

def sub(a,b):
  return a-b

# print(sub(9,9))
print("9,9 ",sum(9,9),sub(9,9))

def Bhai(a):
  print(a)
  
Bhai("Hello world.")

# A R,   A NR,   NA R,   NA NR

# built in function  | user defined function

print("Devendra",end=" ") # by defualt end is \n 
print("Kumar") # this print with Devendra
print("Mandal") # this will print in new line..

# default value  to egnore null valure error

def mul(a=0,b=1):
  print(a//b) # // floor division
  
mul()
mul(3,2)

# def greet(name,dept="SRGC",at) 
# error default argu not in between / before a argument..


def greet(name,dept ,at="SRGC"):
  print("Hi",name)
  print(f"Are you from {dept}  department")
  print("College ",at)
 
# positional argument must know position of varial in function 
greet("Devendra","BCA")

# Keyword argument position not metter
greet(dept="BCA",name="Devendra")
greet(name="Devendra",dept="BCA")

# keyword + positional
greet("Devendra",dept="BCA")# no error
# greet(dept="BCA","Devendra")# error

# Default argument
greet(dept="BCA",name="Devendra",at="DAV")

# arbetri argument | ask non keyworded
def add(*num): #argument convert in tuple no keyword argument aceptable
  c=0
  for i in num:
    c=c+i
  print(c)
  
add (1,2,3,4,5,6,7,8,9,10) 

# keyworded ask argu
def info(**info): #argument convert in dictionary no keyword argument aceptable
  print("\n")
  for key,value in info.items():
    print(key,"=",value  )

info(name="Devendra",Id="23023423",Roll="25",Marks="78",Sub="Computer science") 
info(name="Devendra",Id="23023423") 
info(name="Devendra",Id="23023423",ask="?") 

# add(*num,**data) no error 
# add(**data, *num) syntax error

