"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values
"""


fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File doesn't exist")
    quit()

total=0
count=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        finding=line.find(':')
        number=line[finding+1:].strip()
        num=float(number)
        total=total+num
average=total/count
print("Average spam confidence:",average)
