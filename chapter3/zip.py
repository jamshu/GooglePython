import zipfile
def zip1(zipf,l):
  zipfile1 = zipfile.ZipFile(zipf,'w')
  for name in l:
    zipfile1.write(name)
  for i in zipfile1.namelist():
    print i
zip1('a.zip',['weget.py','extcount.py'])


