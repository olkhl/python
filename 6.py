try:
    fname = open(input("Enter file name: "))
except:
    print ("ERROR: Invalid file name")
    exit()
lst = list()
f = file.read()
f = f.strip().split()
for a in f:
    if a in lst:
        continue
    else:
        lst.append(a)
lst.sort()
print (lst)




fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for i in fh:
    i = i.strip()
    if not i.startswith('From '):
        continue
    emails = i.split()
    print(emails[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
