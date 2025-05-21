#  To-Do list...

task=[]
done=[]

# add task function
def addtask():
    taskIs=input('Enter task : ').upper()
    task.append(taskIs)
    done.append('no')
    print('Task added.')
    
# remove task function
def removeTask():
    if len(task)>0:
      taskIs=input('Enter task name ').upper()
      ind=task.index(taskIs)
      task.pop(ind)
      done.pop(ind)
      print('Task deleted.')
    else:
      print('No task')

# mark as done function
def markAsDone():
    taskIs=input('Enter task name ').upper()
    ind=task.index(taskIs)
    done[ind]='yes'


# get print all tasks 
def GetTask():
    if(len(task)>0):
      print('Task \t Done')
      for i in range(len(task)):
        print(task[i],"\t",done[i])
    else:
      print('Task Empty | Add task')


# task implimentaion
while True :
  num=int(input('1 addTask | 2 mark as done | 3 delete task | 4 Exit : '))
  match(num):
      case 1:
          addtask()
          GetTask()
      case 2:
          markAsDone()
          GetTask()
      case 3:
          removeTask()
          GetTask()
      case 4:
        break
      case _ :
          print('Not a vaild input ')
  
