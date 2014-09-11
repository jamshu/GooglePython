import itertools
def all_perms(elements):
  print list(itertools.permutations(elements, len(elements)))
    
print all_perms([1,2,3,5])
