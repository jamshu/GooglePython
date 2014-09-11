#print directory tree.

import os
import sys
import re
def directorytree(dirname):
  list1=[]
  list2=[]
  list3=[]
  list4=[]
  for dirname,dirnames, filenames in os.walk(dirname):
    for subdirname in dirnames:
        list2.append(os.path.join(dirname, subdirname))
    for filename in filenames:
        list1.append(os.path.join(dirname, filename))
  list3= list1+list2
  list4= sorted(list3,key=len)
  for i in list4:
    print i
  
directorytree(sys.argv[1])
