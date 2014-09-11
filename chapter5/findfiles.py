import os
import re
def findfiles(directory):
  files=os.listdir(directory)
  count=0
  for i in files: 
    if re.search('.py',i):
      count +=1
  print 'number of python files:', count
findfiles('test')
