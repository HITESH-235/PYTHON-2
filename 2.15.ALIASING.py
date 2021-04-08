a = [81,82,83]

b = [81,82,83]

print(a is b) #Since we have not conformed that a=b, therefore there ids are diofferent, so False
print(a == b) #But this method compares value, so True

a = b #a is equivalent to b.(Actually a clone but not completely)(read 'bout it in next file)

print(a is b) #In line 9, we made 'a' equivalent(incomplete clone) to 'b', or vice versa, if we write 'b = a'.
b[0] = 1
 
print(a) #since we changed 'b', and 'a' is equivalent to 'b', so 'a' would be changed too. 

a[0] = 2 #But, but, but, a clone can change root list coz we didn't wrote "a = b[:]" in line 8.
#you will read 'bout "a = b[:]" in next file.
print(b) #so a root list has changed