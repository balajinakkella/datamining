#finalised approach for bag of words method
from collections import Counter
#from Tkinetr import *
import string


#----->
#counter function implementation…

fin=raw_input("INPUT:")
fout=raw_input("OUTPUT:")
fo=open(fin,"r")
data=fo.read(100);
fo.close()


#---->
temp=data
print "Test Tokens:",Counter(data.split())

#--->
#reading stopword filter document
def read_words():
    filter_file=raw_input("FILTER:")
    open_file = open(filter_file, 'r')
    words_list =[]
    contents = open_file.readlines()
    for i in range(len(contents)):
         words_list.append(contents[i].strip('\n'))
    return words_list    
    open_file.close()  


#--->
#function for stopword filter
def diff(a, b):
    return [aa for aa in a if aa not in b]


#----->
#stopword filter
common_words = read_words()
bag_collections=data.split()
finalise_bag=[]
finalise_bag = diff(bag_collections,common_words)
print "Initial Tokens:",Counter(finalise_bag)


#----->
#stemming into root words
finalise_bag1=[]
#print finalise_bag1
for a in finalise_bag:
    b = int(len(a))
    c = (b - 3) 
    d = (b - 2)
    e = (b - 1)
    if a.endswith('ing'):
       if c <= 2:
          #print(a)
          finalise_bag1.append(a)
          #print finalise_bag1
       else:
          #print(a[0:c])
          finalise_bag1.append(a[0:c])
          #print finalise_bag1
    if a.endswith('ed'):
       if d <= 2:
          #print(a)
          finalise_bag1.append(a)
          #print finalise_bag1
       else:
          #print(a[0:d])
          finalise_bag1.append(a[0:d])
          #print finalise_bag1
    if a.endswith('s'):
       if e <= 2:
          #print(a)
          finalise_bag1.append(a)
          #print finalise_bag1
       else:
          #print(a[0:e])
          finalise_bag1.append(a[0:e])
          #print finalise_bag1
    else:
        finalise_bag1.append(a)
        #print finalise_bag1
finalise_bag2=Counter(finalise_bag1)
print "After Stemming:",finalise_bag2

#writing to output.txt file
#f = open(fout,'w')
#f.write('hi there\n')
#f.close


message="frequency of words in the given document is as follows\n"

with open(fout, "w") as text_file:
    text_file.write(message)
    for i in finalise_bag2:
        str1=i+" "
        str2=str(finalise_bag2[i])+"\n"
        str3=str1+str2
        text_file.write(str3)
    text_file.close()
