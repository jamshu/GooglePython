def flatten_list(list1,result=None):
  if result==None:
    result=[]
  for i in list1:
    if isinstance(i,list):
      flatten_list(i,result)
    else:
      result.append(i)
  return result
#print flatten_list([ [1, 2, [3, 4] ], [5, 6], 7])
