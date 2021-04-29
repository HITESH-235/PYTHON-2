x = open(r"2.30.CSV_FILE.csv","w")

z = 0

for a in range(1,13):

    for y in range(1,13):

        z = z + a

        b = (str(y) + "," + str(z))

        x.write(b)

        x.write("\n")

    z = 0
    
    x.write("\n")
