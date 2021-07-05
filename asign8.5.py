"""
Exercise  8.5: Write a program to read through the mail box data and when you
find the line that starts with "From", you will split the line into words
using the split function. We are interested in who sent the message, which is
second word on the From line.
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
You will parse the From line and print out the second word for each From line,
then you will also count the number of From (not From:) lines and print out a
count at the end.

"""


fname = input("Enter file name: ")
fh = open(fname)
count = 0
for str in fh:
    line=str.split()
    if len(line) < 3 or line[0]!='From':
        continue
    print(line[1])
    count=count+1

print("There were", count, "lines in the file with From as the first word")
