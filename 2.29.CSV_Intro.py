#CSV stands for Comma Separated Values. If you print out tabular data in CSV format, it can be easily imported into other programs like Excel, Google spreadsheets, or a statistics package (R, stata, SPSS, etc.).
#For example, we can make a file with the contents of last file. If you save it as a file name grades.csv, then you could import it into one of those programs. The first line gives the column names and the later lines each give the data for one row.

fileconnection = open(r"2.28.CSV_File.csv", 'r')

lines = fileconnection.readlines()

header = lines[0]

field_names = header.strip().split(',')#we have written strip(), just to remove the last enter to be printed while running

print(field_names)

for row in lines[1:]:

    vals = row.strip().split(',')

    if vals[5] != "NA":

        print("{}: {}; {}".format(vals[0],vals[4],vals[5]))

#How will a program processing a .csv file know when a comma is separating columns, and when it is just part of the text string giving a value within a column?

#The CSV format is actually a little more general than we have described and has a couple of solutions for that problem. One alternative format uses a different column separator, such as | or a tab (t). Sometimes, when a tab is used, the format is called tsv, for tab-separated values). If you get a file using a different separator, you can just call the .split('|') or .split('\\t').

#The other advanced CSV format uses commas to separate but encloses all values in double quotes.

#For example, the data file might look like:

#"Name","Sex","Age","Team","Event","Medal"
#"A Dijiang","M","24","China","Basketball","NA"
#"Edgar Lindenau Aabye","M","34","Denmark/Sweden","Tug-Of-War","Gold"
#"Christine Jacoba Aaftink","F","21","Netherlands","Speed Skating, 1500M","NA"
#If you are reading a .csv file that has enclosed all values in double quotes, it’s actually a pretty tricky programming problem to split the text for one row into a list of values. You won’t want to try to do it directly. Instead, you should use python’s built-in csv module. However, there’s a bit of a learning curve for that, and we find that people gain a better understanding of reading CSV format by first learning to read the simple, unquoted format and split lines on commas.
