a=5.0
b=5

print(id(a),id(b)) #returns the memory addresses where the objects a and b are stored.

print(a is b) # false 
print(a==b) # true
print(a is not b) #true

# Membership operator

str="Devendra"

print("y" in str) #false
print("D" in str) #true
print("Deve" in str) #true
print("D" not in str) #false

lis=[1,2,3,4,5]

print(6 not in lis)
print(5 in lis)

print(round(1.2589645,3))
print(round(1.61)) # 2 int
print(round(6761,-2)) # 
print(round(1.61,0)) # 2 float
print(round(2.5)) # 2   nearest even number
print(round(1.5)) # 2   nearest even number