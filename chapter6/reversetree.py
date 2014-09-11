def reversetree(list1):
  list1.reverse()
  for i in list1:
   if isinstance(i,list):
     reversetree(i)
  return list1

print reversetree([[1,2],[3,[4,5]],6])  
