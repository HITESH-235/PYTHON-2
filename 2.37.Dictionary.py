#This file will be an additional part to last file no. 36
#We will again use dictinaries when reading a file

x = open(r'2.35.Text_File.txt','r')

y = x.read()

d = {} #Empty dictionary

for z in y:

    if z not in d:
        d[z] = 0 #automatically initialize z's value as 0, when not found in dict.

    d[z]+= 1

print('Letter "a" has',d['a'],'occurences')
print('Letter "h" has',d['h'],'occurences')
