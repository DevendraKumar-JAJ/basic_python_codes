class Student:
  def __init__(self,name,house):
    self._name=name
    self.__house=house
  def getData(self):
    print(f"Hello, {self._name}!")
    print(f"You are from  {self.__house}!")
def main():
  s1=Student("Devendra","Harhanja")
  s1.house="hjh"
  s1._name="dev"
  s1.getData()
  
  nmae="🤣"
  print(ord(nmae))
      
      
# if __name__==__main__:
main()