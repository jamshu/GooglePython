#Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.
import sys
f=open(sys.argv[1],'r')
text=f.readlines()
print 'head lines: '
for i in text[:10]:
  print i[:-1]
print 'tile lines: '
for i in text[-10:]:
  print i[:-1]
