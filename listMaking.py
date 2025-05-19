L1=[]

while True:
    num=int(input('List size: '))
    if(num>=0):
        break

while num>0:
    item=input('Enter elements : ')
    L1.append(item)
    num-=1

print(L1)