"""
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
"""


fname = input("Enter file name: ")
new=[]
fh = open(fname)
for name in fh :
    word=name.split()
    
    for words in word:
        if words in new:
            continue
        new.append(words)
print(sorted(new))
