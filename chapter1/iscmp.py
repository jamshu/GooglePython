#Write a function iscmp to compare two strings, ignoring the case.
def iscmp(s1,s2):
  if s1.upper()==s2.upper():
    return 'true'
  else:
    return 'false'
print 'enter first string'
a=raw_input()
print 'enter second string'
b=raw_input()
print iscmp(a ,b)
