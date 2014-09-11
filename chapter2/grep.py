#implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.
import sys
f=open(sys.argv[1],'r')
text=f.readlines()
a=sys.argv[2]
for i in text:
  if a in i:
    print i
