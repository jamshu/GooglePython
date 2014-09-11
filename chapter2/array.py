#Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:
def array(n1,n2):
 
 list1=[[None]*n2 for i in range(n1)]
 print list1
 return list1
 
def addvalue(r,c,n,list1):
  list1[r-1][c-1]=n
  print list1  
array(4,3)
addvalue(1,2,5,array(4,3))



