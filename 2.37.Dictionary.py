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

x.close()

#now we will write code to calculate points in scrabble game
#Suppose there is 10 points on letter 'a' and 20 points on letter 'h'

x1 = open(r'2.35.Text_File.txt','r')

y1 = x1.read()

d1 = {}

for z1 in y1:

    if z1 not in d1:
        d1[z1] = 0

    d1[z1]+= 1

d2 = {'a': 10, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':20, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

a = 0

for z2 in d1:

    if z2 in d2:
        a+= (d1[z2]*d2[z2])

print(a)

x1.close()

