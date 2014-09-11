#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def get_special_path(dir1):
  f=os.listdir(dir1)
  list1=[]
  for i in f:
    list1.append(os.path.abspath(os.path.join(dir1,i)))
  return list1
  return 

def copy_to(paths,dir1):
  for i in paths:
    shutil.copy2(i,dir1)
  print 'copy done'  
def zip_to(paths,zippath):
  for i in paths:
    cmd= 'zip -j'+' ' +zippath+' '+ i
    output=commands.getoutput(cmd)
  print output
# Write functions and modify main() to call them



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  get_special_path(sys.argv[1])
  copy_to(get_special_path(sys.argv[1]),sys.argv[2])
  zip_to(get_special_path(sys.argv[1]),sys.argv[3])
  # Call your functions
  
if __name__ == "__main__":
  main()
