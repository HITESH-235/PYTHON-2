x = ("a","b",1,"c",2,"d","e","f")

print(x[2]) #prints 1

print(x[2:6]) #prints 1 to "d"

#Figure out the difference between writing nos., from nos. with colons.

x = x[:3] + ("y",3) + x[5:]

print(x)

