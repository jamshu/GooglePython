#Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.
import sys
def wrap(filename,width):
  f=open(filename,'r')
  text=f.read()
  print text
  i=0;
  list1=[]
 # while i<(len(text)/int(width)):
  while i<len(text):
    list1.append(text[:int(width)])
    text=text[int(width):]
    i=i+int(width)
  for i in list1:
    print i
wrap(sys.argv[1],sys.argv[2])
