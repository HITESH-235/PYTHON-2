print("a" in 'apple') #True

print("ap" in 'apple') #True

print('pa' in 'apple') #False

print('a' not in 'apple') #False

print('a' in ['a','ball','cat']) #Since there's an individual element 'a' in list, so True
print('a' not in ['a','ball','cat']) # False

print('a' in ['apple','absolute','application','nope']) #Since one element doesn't includes 'a', so False
print('a' not in ['apple','absolute','application','nope']) #True
print('a' in ['apple','absolute','application']) #since all element includes 'a', so True
print('a' not in ['apple','absolute','application']) #False