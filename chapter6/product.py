def product(a,b):
  if a==0 or b==0:
    return 0
  else:
    return a+ product(a,b-1)
print product(4,5)
