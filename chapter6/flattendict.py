def flatten_dict(dict1,result=None,key=None):
  if result==None:
    result={}
  if key==None:
   key=[]
  for k,v in dict1.items():
    if isinstance(v,dict):
      flatten_dict(v,result,key+[k])
    else:
      result['.'.join(key+[k])]=v
  return result
print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
