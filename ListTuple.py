a=[1,2,3,4,5,6,7,8,9,10] # List
b=(1,2,3,4,5,6,7,8,9,10) # Tuple

print(a[5:])# [6, 7, 8, 9, 10]
print(b[5:])# (6, 7, 8, 9, 10)
print(a[5:9])# [6, 7, 8, 9]
print(b[5:9])# (6, 7, 8, 9)
print(a[5:9:2])# [6, 8]
print(b[5:9:2])# (6, 8)
print(a[5:9:3])# [6, 9]
print(b[5:9:3])# (6, 9)
print(a[5:9:4])# [6] 
print(b[5:9:4])# (6,)
print(a[5:9:5])# [6]
print(b[5:9:5])# (6,)
print(a[5:9:6])# [6]
print(b[5:9:6])# (6,)
print(a[5:9])# [6, 7, 8, 9]
print(b[5:9])# (6, 7, 8, 9)
print(a)
a.append(11)
print(a)  
print(a.sort(reverse=True))# return None  Descending order
print(a)
c=["Raj","Rahul","Devendra","Rajesh","Ravi"]
d=("Raj","Rahul","Devendra","Rajesh","Ravi") # Tuple wil not support sort() method.
c.sort()# Ascending order
print(c)# ['Devendra', 'Raj', 'Rajesh', 'Rahul', 'Ravi']
c.remove("Raj")
print(c)# ['Devendra', 'Rajesh', 'Rahul', 'Ravi']
c.pop(2)
print(c)# ['Devendra', 'Rajesh', 'Ravi']
c.insert(2,"Rahul")
print(c)# ['Devendra', 'Rajesh', 'Rahul', 'Ravi']
c.reverse()
print(c)# ['Ravi', 'Rahul', 'Rajesh', 'Devendra']
c[0]="Raj"
print(c)# ['Raj', 'Rahul', 'Rajesh', 'Devendra']
# b(2)=5 # Tuple object does not support item assignment.
e=(1) #this is not a tuple
f=("Devendra")# Not a tuple
g=(1,) # is a tuple becuase there is a coma in the end of 1 data.
h=(1,2,) # here the last coma is optional 2,