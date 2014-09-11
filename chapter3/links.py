import re
import os
def links(filename):
 index=open(os.path.join('text',filename),'r')
 for i in index:
   if 'http' in i: 
     match=re.search(r'http+[\w+/+:._-]+"',i)
     if match:
       print match.group()
links('index.html')
