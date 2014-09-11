#Write a regular expression to validate a phone number.

import sys
import re
def phone(number):
  if len(number)==10:
    a=re.search('\d+',number)
    n=a.group()
    if(len(n)==10):
      print 'Phone number is Valid'
  else:
      print 'Phone number is not Valid'
phone(sys.argv[1])
