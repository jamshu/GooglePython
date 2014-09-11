#Write a program center_align.py to center align all lines in the given file.
import sys
def centre(filename):
  f=open(filename,'r')
  text=f.readlines()
  widths=[]
  add=[]
  for i in text:
    widths.append(len(i))
  maxim=(max(widths))/2
  for i in text:
    wid=len(i)/2
    if wid<maxim:
      diff=maxim-wid
      while(diff>0):
        i=' '+i
        diff=diff-1
    print i[:-1]
centre(sys.argv[1])
