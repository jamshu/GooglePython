import time
def square(x):
  return x * x
def profile(f):
  dict1={}
  list1=[]
  def g(x):
    if x not in dict1:
       start=time.time()
       dict1[x]=f(x)
       end=time.time()
       t=end-start
       return t
    return list1
  return g
f= profile(square)
print f(10)

