import os
import re
def findfiles(directory):
  files=os.listdir(directory)
  for i in files:
    path=os.path.abspath(os.path.join(directory, i))
    count=0
    if re.search('.py',i):
      f=open(path,'r')
      text=f.readlines()
      for j in text:
        count=count+1
      f.close()
      print 'number of codes in file ', i, 'is ',count
findfiles('test')

