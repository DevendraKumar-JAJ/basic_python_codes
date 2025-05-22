import time
if "10"<"2":  #true
  print("Hello")
  
if "100"<"2": #false why
  print('Yes')
  
x=11
[print(x) if x>10 else print(10)]


while(user_input:=input()):
  print('Press Enter Key to stop loop else enter any char.')
  print(f"You Enterd : {user_input}")
  
  
x = 6
y = "big" if (z := x * 2) > 10 else "small"
print(y, z)



numbers = [x for x in range(10) if (y := x * 2) > 5]
print(y)  # Note: y will be the last value assigned

print(numbers)



#  Typewriter effect 

text='Hello Devendra! \n And I am web Developer. '
for char in text :
  print(char,end='',flush=True)
  time.sleep(0.05)



  
