#Write a function mutate to compute all words generated by a single mutation on a given word. A mutation is defined as inserting a character, deleting a character, replacing a character, or swapping 2 consecutive characters in a string. For simplicity consider only letters from a to z.
def mutate1(str1,str2):
  if len(str1)+1==len(str2):
    if str2.find(str1) != -1:
       print True
       return True
    else:
       print False
       return False
  elif  len(str1)==len(str2):
      if str1==str2:
         print True
         return False
      elif str1!=str2:
         j=0
         for i in str2:
           if i not in str1:
             j=j+1
         if j==0:
            print True
            return True
         else:
            print False
            return False         
      else:
         k=0
         for i in str2:
           if i not in str1:
             k=k+1
         if k==1:
             print True
             return True
         else:
             print False
             return False
  elif len(str1)==len(str2)+1:
      if str1.find(str2) != -1:
       print True
       return True
      else:
       print False
       return False
  

      
mutate1('ashif','ashif')

