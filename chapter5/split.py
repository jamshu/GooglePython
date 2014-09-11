import os
import sys
def split(filename,n):
 #filepath= path=os.path.abspath(os.path.join(directory, filename))
 f=open(filename,'r')
 text=f.readlines()
 j=1
 i=0
 lng=len(text)
 while i <lng:
   fname='file%d'% j
   print fname
   i+=n
   j+=1
   index = open(os.path.join('test', fname), 'w')
   for k in text[:n]:
      index.write(k)
#      text=text[n:]
   index.close()
   text=text[n:]

split('problem2.py',3)
