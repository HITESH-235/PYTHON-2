x = [("John Aalberg", 31, "Cross Country Skiing, 15KM"),
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

y = open("2.32.CSV_File.csv", "w")
# output the header row
y.write('"Name","Age","Sport"')

y.write('\n')
# output each of the rows:
for z in x:

    a = ",".join([z[0], str(z[1]), z[2]])

    y.write(a)

    y.write('\n')

y.close()
