# numIs=int(input('Enter  your number '))
# numCopy=numIs
# newNum=0
# count=0
# # count number of digits in number
# while (numCopy>0):
#   count+=1
#   numCopy//=10

# # creating reverse of number
# numCopy=numIs
# while(numCopy>0):
#   temp=numCopy%10
#   newNum=newNum*10+temp
#   numCopy//=10
  
# # checking both are same or not
# if(newNum==numIs):
#   print('Pelindrome')  
# else:
#   print('Non pelindrome ')
  
  
# # 

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
    newNum=newNum*10+temp
    numCopy//=10
    
  # checking both are same or not
  if(newNum==vali):
    print(vali ,end=' ')  
  
  