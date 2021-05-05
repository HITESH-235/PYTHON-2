x = open(r'2.35.Text_File.txt','r')

y = x.read()

z = 0
z1 = 0

for a in y:
    if a == 'a':#counts no. of 'a's in the file
        z+=1
    elif a == 'h':
        z1+=1

print('Letter "a" has',z,'occurences')

print('Letter "h" has',z1,'occurences')

x.close()
#so this was a simple example how you can count a letter inside another file
#now we will be adding use of dictionaries here in same example

x = open(r'2.35.Text_File.txt','r')

y = x.read()

z = {}

z['a'] = 0
z['h'] = 0

for a in y:

    if a == 'a':
        z[a]+=1 #since a='a' for now, so, z['a']=z[a]
    elif a == 'h':
        z[a]+=1 #since a='h' for now, so, z['h']=z[a]

print('------------------------------')

print('Letter "a" has',z['a'],'occurences')

print('Letter "h" has',z['h'],'occurences')
