while True:
  try:
    x=int(input("Enter X "))
  except  ValueError:
    print("X is not a integer...")
  else:
    print(f"X is {x} : Integer type ")
    break
  

def validate_age(age): 
    if age < 18:
        raise ValueError("Age must be 18 or older")
    else:
        print("Age is valid")

validate_age(x) #raising error  argument must be greater than or equal to 18