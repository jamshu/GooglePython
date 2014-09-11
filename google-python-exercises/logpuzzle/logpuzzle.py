#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  match=re.search('_\S+',filename)
  host= match.group()[1:]
  f=open(filename,'r')
  text=f.read()
  match=re.findall(r'GET\s(\S+)',text)
  list1=[]
  list2=[]
  for i in  match:
    if 'puzzle' in i:
      if i not in list1:
        list1.append(i)
  for i in sorted(list1):
  #    print 'http://'+host+i
      list2.append('http://'+host+i)
  print list2 
  return list2 
   
def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
 
  index=open(dest_dir,'w')
  index.write('<html>\n<body>')
  j=0
  f2=dest_dir[:-5]
  for i in img_urls:
  #  local_name = 'img%d' % j
    index.write('<img src="%s">' % i)
    j=j+1
  index.write('\n</body>\n</html>\n')
  index.close()
  # +++your code here+++
  

def main():
 # args = sys.argv[1:]

  #if not args:

 # todir = ''
 # if args[0] == '--todir':
  #  todir = args[1]
   # del args[0:2]

 # img_urls = read_urls(args[0])

 # if todir:
  #  download_images(img_urls, todir)
  #else:
   # print '\n'.join(img_urls)
 read_urls(sys.argv[1])
 download_images(read_urls(sys.argv[1]),sys.argv[2])
if __name__ == '__main__':
  main()
