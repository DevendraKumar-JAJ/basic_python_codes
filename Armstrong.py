# Armstrong Number Finder

# A Python program that finds Armstrong numbers within a given range.

# What is an Armstrong Number?

# An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

# Features

# - Finds Armstrong numbers within a given range
# - Validates user input to ensure start number is greater than 0 and less than or equal to end number
# - Prints Armstrong numbers in the given range

# Usage

# 1. Run the program
# 2. Enter the start number
# 3. Enter the end number
# 4. The program will print Armstrong numbers in the given range

# Code

# The code is written in Python and uses a simple iterative approach to find Armstrong numbers.

# Requirements

# - Python 3.x




import math
startNum=int(input('Enter start number  '))
endNum=int(input('Enter end number  '))
while True:
  if(startNum<1):
    startNum=int(input('Enter start number  '))
  elif(startNum>endNum):
    endNum=int(input('Enter end number '))
  else:
    break

for vali in range (startNum,endNum+1):
  numCopy=vali
  newNum=0
  count=0
  # count number of digits in number
  while (numCopy>0):
    count+=1
    numCopy//=10
  
  # creating reverse of number
  numCopy=vali
  while(numCopy>0):
    temp=numCopy%10
    sqr=math.pow(temp,count)
    newNum=newNum+sqr
    numCopy//=10
    
  # checking both are same or not
  if(newNum==vali):
    print(vali ,end=' ')  
  
  