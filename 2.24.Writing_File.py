x = open(r"#.3.Dummy_File3.html","w")

y = "THIS HAS BEEN WRITTEN BY ME"

x.write(y)

x.close()

#CHECKOUT THE FILE NOW

#writing a file empties the file going to be opened and stores new value that we give.
#so be careful, so that your useful data won't get lost.
#write() always takes strings, so if y is int, change it to str.
#or even write("hfbvhsvb").
#But if a file you run to write in doesn't exists, then it will create a new file with the name you gave.
#Here's an example

x = open(r"Delete_this.txt","w")

y = "PLEASE DELETE THE FILE AFTER USE"

x.write(y)

x.close()

#CHECKOUT THE FILE NOW

#you can even read a file inside writing into another file.
#you can also say it "copies" the root file content into another file.
#Here's an example

x = open(r"#.3.Dummy_File3.html","w")

y = open(r"#.2.Dummy_File2.html","r")

z = y.read()

x.write(z)

x.close()

#CHECKOUT BOTH THE FILES NOW AND YOU WILL SEE THE TEXT HAS BEEN COPIED.
