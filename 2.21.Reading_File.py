x = open(r"#.2.Dummy_File2.html","r")

y = x.read()
print(y) #prints whole file

print("x---------------x")

x.close()

x = open(r"#.2.Dummy_File2.html",'r')

z = x.read(100)
print(z) #prints first 100 letters

x.close()
