import re
s='<tr align="right"><td>1</td><td>Jacob</td><td>Emily</td>'
#a=re.search('[\w.-]+@[\w.-]+',s)
a=re.search(r'[\s+]+<',s)
print a.group()

