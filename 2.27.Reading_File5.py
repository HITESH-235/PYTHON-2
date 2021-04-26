with open(r"#.2.Dummy_File2.html",'r') as x:

    print(x.readline()) #prints just one line

x.close()

#The cursor inside readline(x) works like this
#(-infinity) < x >= (-1) = every character of first line
# x = 0 = nothing
# x = 1 = prints 1st character
# And so on..........

with open(r"#.2.Dummy_File2.html",'r') as x:

    print(x.readlines()) #prints every line in a different way(inside a list)

x.close()

#The cursor inside readlines(x) works like this
#(-infinity) < x >= (-1) = every line
# x = 0 = every line
# 1 <= x >= 21 = first line (#the line has 21 characters) #21
# 22 <= x >= 43 = 1st, 2nd line #21+0+21+1
# 44 <= x >= 65 = 1st, 2nd, 3rd line #21+0+21+1+21+1
# 66 <= x >= 87 = 1st, 2nd, 3rd, 4th line #21+0+21+1+21+1+21+1
# 88 <= x > infinity = 1st, 2nd, 3rd, 4th, 5th line #21+0+21+1+21+1+21+1+21+1
print()
with open(r"#.2.Dummy_File2.html",'r') as x:

    y = (x.readlines())

    for z in y[:5]:
        print(z)

x.close()

