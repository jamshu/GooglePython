#Write a python function parse_csv to parse csv (comma separated values) files
import sys
def csw(filename):
  f=open(filename,'r')
  text= f.readlines()
  list1=[]
  for i in text:
    list1=i[:-1].split(',')
    print list1
csw(sys.argv[1])
    
