#Write a function group(list, size) that take a list and splits into smaller lists of given size.
def group(l,size):
   limit= (len(l)/size)
   i=0
   list1=[]
   while i <= limit:
     a=l[:size]
     l=l[size:]
     list1.append(a)
     i=i+1
   print list1
group([1,3,4,5,6,7,8,5,9,6],3)
