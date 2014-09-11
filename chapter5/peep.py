def peep(it):
  try:
   list1=[]
   while True:
     list1.append(it.next())
  except:
    print ''
  finally:
    print list1[0],list1
peep(iter(range(5)))
peep(iter([1,2,6,3,9]))
