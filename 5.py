# Use words.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    print("wrong file name", fname)
x = fh.read()
a = x.upper()
a = a.rstrip()
print(a)
