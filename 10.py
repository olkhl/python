#10.2

fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
z = list()
lists = list()
for i in fh:
    i = i.strip()
    if not i.startswith('From '):
        continue
    emails = i.split()
    time = emails[5]
    times = time.split(":")
    hours = times[0]
    z.append(hours)


for name in z:
	counts[name] = counts.get(name,0) + 1

for k,v in sorted(counts.items()):
	newtup = (int(k),v)
	lists.append(newtup)
	print(k,v)
