def square(x):
  return x * x
def vectorize(f):
  dict1={}
  list1=[]
  def g(x):
    for i in x:  
       dict1[i]=f(i)
       list1.append(dict1[i])
    return list1
  return g
f=vectorize(len)
print f(['1','2','3sdc'])
#print f([[1,2],[3,5]])      
