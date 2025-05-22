L1=[1,8,5,9,3,7,6,8,9,10,0,-1]

grater=L1[0]
sum=0
smaller=L1[0]

for val in L1:
    sum+=val
    if(grater<val):
        grater=val
    if(smaller>val):
        smaller=val



print('Greater in list: ',grater)
print('Smaller in list: ',smaller)
print('Sum all elements of list :',sum)