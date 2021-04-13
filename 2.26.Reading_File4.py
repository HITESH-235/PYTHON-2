#There exist a method which is a substitute to the "x = open(---)" method.
#For Loop when Reading a File
with open(r"#.2.Dummy_File2.html",'r') as x:

    #print(x.read())
    #print("--------------")

    for y in x:

        print(y) #You can also do that of line 5, but this method will print each line separately

x.close()
