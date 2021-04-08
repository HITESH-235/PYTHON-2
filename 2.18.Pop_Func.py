x = [12,24,48,34]

y = x.pop() #removes last element and stores in y.

print(x)#x will be unchanged.

print(y) #y = 34
# x is now equal to [12,24,48]
z = x.pop(0) #removes 1st element(you can try changing the index value)
# x is now equal to [24,48]
z1 = x.pop(-1) #removes last element
# x is now equal to [24]
print(x) #[24]

print(z) #12

print(z1) #48