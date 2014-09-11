import re
f=open('animal_code.google.txt','r')
text=f.read()
match=re.search('_\w+',text)
print match.group()
