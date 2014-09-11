import urllib2  
import os
import sys
def weget1(url):
 file = urllib2.urlopen(url)
 if os.path.basename(url):
   htmlname=os.path.basename(url)
 else:
   htmlname='index.html'
 file1=os.path.join('text', htmlname)
 index=open(file1,'w')
 for line in file: 
   index.write(line)
 
weget1('http://docs.python.org/tutorial/')

#weget('http://docs.python.org/tutorial/interpreter.html')
