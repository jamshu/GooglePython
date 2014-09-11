#mplement a function fact, to compute factorial of a  of a number.
def product(l):
  pr=1
  for i in l:
    pr=pr*i
  print pr
def fact(n):
  list1=[]
  for i in range(n+1)[1:]:
   list1.append(i)
  product(list1)
fact(5)
