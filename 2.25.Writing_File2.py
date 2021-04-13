#FOR LOOP WHEN WRITING IN A FILE

x = open(r"#.3.Dummy_File3.html",'w')
#A PROGRAM WHICH WILL WRITE SQUARES FROM 1 TO 50) IN ANOTHER FILE

for n in range(1,51):

    sqr = n*n

    x.write(str(sqr))

    x.write("\n")

x.close()
#CHECKOUT THE FILE

x = open(r"#.3.Dummy_file3.html",'r')

print(x.read())

x.close()
