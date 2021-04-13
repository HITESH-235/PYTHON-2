x = open(r"C:\Users\HITESH\OneDrive\Desktop\HTML_FILES\1.1.First_HTML.html","r")

print(x.read())

x.close()

print('x----------O-R----------x')

x = open(r"..\..\HTML_FILES\1.2.Ordered_lists.html","r")
#Sometimes there are unwanted errors in opening a file, so try writing "..\" 2 times

print(x.read())

x.close()

# Some computers may give error if that r is not written, mine gave errors, so I wrote.
