def treemap(list1):
  list2=[]
  for i in list1:
   if isinstance(i,list):
      treemap(i)
   else:
      list2.append(i*i)
  return list1
 
print treemap([1, 2, [3, 4, [5]]])
