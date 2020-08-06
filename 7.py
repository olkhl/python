name = input('file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bc = None
bw = None
for word,count in counts.items():
    if bc is None or count > bc:
        bc = count
        bw = word
print(bw, bc)
