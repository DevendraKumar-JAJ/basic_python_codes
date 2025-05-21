def show(n):
  if(n==0): #must have a base case... use to stop calling at a time
    return
  print(n , end="\t")
  show(n-1) #this print reverse like n to 1
  
show(5)

# recursion is a function which call them self repeatly ...

# Factorial using recursion 
def fact(n):
  if(n==0 or n==1):
    return 1
  return fact(n-1)*n

print("\n",fact(5))