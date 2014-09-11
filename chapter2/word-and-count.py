#Improve the above program to print the words in the descending order of the number of occurrences.
import sys
def wordcountsort(filename):
  f=open(filename,'r')
  dict1={}
  text=(f.read()).split()
  for i in text:
   if i not in dict1:
     dict1[i]=1
   else:
     dict1[i]=dict1[i]+1
  print dict1
  for i in sorted(dict1.items(),reverse=True):
     print i
wordcountsort(sys.argv[1])
