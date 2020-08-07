name = input('file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in [:10] :
    print (key, val)


#print ( sorted [ (v,k) for k,v in counts.items() ] ), reverse=True)
#list comprehension creates a dynamic list. make list of reversed tuples then sort it
