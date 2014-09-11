def izip(itr1,itr2):
  try:
   dict1={}
   list2=[]
   while True:
    # list1.append(itr1.next())
     dict1[itr1.next()]=itr2.next()
  except:
    print ''
  finally:
    for i in dict1.items():
      print i

izip(iter([1,2,6,3,9]),iter(['a','b','c','d','e']))
  
