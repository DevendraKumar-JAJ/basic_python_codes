import sys
a={
  "name":"devendra",
  "class":"bca",
  "tup":("dev,rajes"),
  "dic":{
    "name":"dev"
  }# nested dic
  }#dic
a["class"]="BBA"
print(a["name"])
print(a["class"])
b={}
print(sys.getsizeof(b))
print(sys.getsizeof(a))
print(list(a.keys()))# keys
print(len(list(a.keys())))# length

print(a.values())

print(list(a.items()))
print(a.get("name"))
a.get("dic").update({"city":"Delhi"})
print(a)


b={1,2,3,4,5}# set 
c={"world",2,2,3,5,4,4,1,"hello"} #save in asending order like
print(b)

print(c)
d={
  int(9),"9.0","hel'l"
}
print(d)

set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set2-set1)
print(set1-set2)
# print(set1+set2)
# print(set2+set1)error
print(set1|set2)#union 
print(set2|set1)#union 
print(set1&set2)#intersection
print(set2&set1)#intersection
print(2|1) #three


print(set1.difference(set2)) #many argument
print(set2.difference(set1))
print(set1.difference_update(set2))
set1={1,2,3}
set2={3,4,5}
print(set1.symmetric_difference(set2)) # not in both | only one argument
print(set1^set2) # same as sd function

print(1^4)

# super set disjiont set etc
 #disjoint set | intersection of sets is empty
set1={1,2,3,4,5}
set2={1,2,3}
set3={6,7,8}
print(set1.isdisjoint(set3))
print(set2.issubset(set1))
print(set1.issuperset(set2))



def pos(a):
  leng=len(a)
  
  return 2**leng

def print_subsets(s):
    n = len(s)
    total = 2 ** n  # calculate total number of subsets

    # convert set to list for indexing
    s = list(s)

    for i in range(total):
        subset = [s[j] for j in range(n) if (i & (1 << j))]
        print(subset)

# test the function
print(pos({1,2,3,4,5}))
print_subsets({1, 2, 3,4,5})

