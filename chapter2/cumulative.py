#Implement 2 functions, to compute comulative product and comulative sum of a list of numbers.
def product(l):
  pr=1
  for i in l:
    pr=pr*i
  return pr

def cumsum(l):
  i=1
  list1=[]
  list2=[]
  while i<len(l)+1:
    list1.append(l[:i])
    i=i+1
  for i in list1:
    list2.append(sum(i))
  print 'cumulative sum is:',list2
def cumpro(l):
  i=1
  list1=[]
  list2=[]
  while i<len(l)+1:
    list1.append(l[:i])
    i=i+1
  mul=1
  for i in list1:
    p=product(i)
    list2.append(p)
  print 'cumulative product is:',list2
cumsum([1,2,3,4])  
cumpro([1,2,3,4])

