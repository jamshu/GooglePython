#program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.

import os
import re
import sys
def extcount(dirname):
  list1=[]
  list2=[]
  dict1={}
  filenames=os.listdir(dirname)
  for i in filenames:
    list1.append(i)
  for i in list1:
    match=re.search('.(\S+)',i)
    list2.append(match.group(1))
  for i in list2:
    if i not in dict1:
       dict1[i]=1
    else: 
       dict1[i]=dict1[i]+1
  for i,j in dict1.items():
    print i,' ',j
extcount(sys.argv[1])

