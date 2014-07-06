#stemming into root words

a = raw_input("Enter the word: ")
b = int(len(a))
c = (b - 3) 
d = (b - 2)
e = (b - 1)
if a.endswith('ing'):
   if c <= 2:
      print(a)
   #elif a[0:c].endswith('v') or a[0:c].endswith('k') or a[0:c].endswith('l'): 
      #print(a[0:c]+'e')
   else:
      print(a[0:c])
if a.endswith('ed'):
   if d <= 2:
      print(a)
   else:
      print(a[0:d])
if a.endswith('s'):
   if e <= 2:
      print(a)
   else:
      print(a[0:e])
