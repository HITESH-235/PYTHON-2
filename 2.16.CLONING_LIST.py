a =  [2,3,4]

b = a[:] #'b' is now a clone of 'a'
#Don't forget to write "[:]" 'coz without it, a clone list,i.e.,"b", will still be able to change root list,i.e.,"a"
#and if "b" can change "a", just 'coz you didn't wrote "[:]", will make an error
print(b)

print(a is b) #Since "b" is just a clone of "a", so it doesn't belongs to "a" anyway, so false
print(b is a) #Again false, 'coz "b" still doesn't belongs to "a", "clone list is completely different from root list"
b[0] = 1

print(a == b) #Now that we have changed "b" a bit, so comparison would give false.

print(a) #"a" is the root list, can't be changed by a change in "b",i.e.,clone list
