def count_change(a,list1):
  if a==0:
   return 1
  if a<0 or len(list1)==0:
   return 0
  d=list1[0]
  return count_change(a,list1[1:])+count_change(a-d,list1)
print count_change(10,(1,5))
