#Implement a function reverse,commpute reverse of a list of numbers.
def reverse(l):
  list1=[]
  for i in l:
    list1.insert(0,i)
  return list1
print reverse([1,2,3,4,5,6])
print reverse(reverse([1,2,3,4,5,6]))

