x = [("Hitesh",89),("A",88),("B",93)] #Pairs can also be made in lists

for y in x:
    name = y[0]
    score = y[1]
    # print("Hello",name,"Your Score Is",score) 

for y in x:
    name = y[0]
    score = y[1]
    print(("Hello {}! Your Score Is {}.").format(name,score))

