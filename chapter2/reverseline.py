#Write a program reverse.py to print lines of a file in reverse order.
import sys
def reverse(filename):
  f=open(filename,'r')
  a= f.readlines()
  for i in a[::-1]:
      print i[:-1]
reverse(sys.argv[1])
