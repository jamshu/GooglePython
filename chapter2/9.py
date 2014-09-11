#improve the unique function written in previous problems to take an optional key function as argument and use the return value of the key function to check for uniqueness
def unique(set1):
  set2=set([])
  for i in set1:
    if i in set2:
      set2.add(i)
  print set2
unique(set[1,3,4,5,4,2,1])
