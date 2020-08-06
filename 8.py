#9.4

fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
z = list()

for i in fh:
    i = i.strip()
    if not i.startswith('From '):
        continue
    emails = i.split()
    z.append(emails[1])
for name in z:
	counts[name] = counts.get(name,0) + 1

bc = None
bw = None
for name,count in counts.items():
    if bc is None or count > bc:
        bc = count
        bw = name
print(bw, bc)
