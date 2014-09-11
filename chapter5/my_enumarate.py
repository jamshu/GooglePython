def my_enumerate(itr):
  try:
    list1=[]
    while True:
      list1.append(itr.next())
  except:
    print ''
  finally:
    j=0
    for i in list1:
      print j,i
      j+=1
my_enumerate(iter([2,4,6,1]))
  
