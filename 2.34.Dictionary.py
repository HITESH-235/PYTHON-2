#Here we are starting dictionary again
#If you haven't seen my first python repository's dicitionary part, check it first from the given link, from file no. 57
# https://github.com/HITESH-235/PYTHON
x = {"apple":100,'banana':90,'pears':95}
print('x was like this before--',x)
y = x
y['pears'] = 50
print('now x is like this--',x)

#in the above code, we saw that y was made a copy of dictionary named 'x'
#but, since dictionaries are mutable, they changed when there copied dictionaries are changeed
#we saw the same here with x and y.
