#rite a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.

import os
import re
import time
import sys
def filedetails(dirname):
  list1=[]
  filename=os.listdir(dirname)
  for i in filename:
    path=os.path.abspath(os.path.join(dirname, i))
    list1.append(path)
  for i in list1:
    f=open(i,'r')
    text=f.read()
    print os.path.basename(i),'\t',len(text),'\t',time.ctime(os.path.getmtime(i))
    f.close()
# text=f.read()
 # print text
  #f.close() 
filedetails(sys.argv[1])

