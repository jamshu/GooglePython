#program to list all files in the given directory

import os
import sys
def listing(dirname):
  filenames=os.listdir(dirname)
  for i in filenames:
    print i
listing(sys.argv[1])
