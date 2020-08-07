import re
name = input('file: ')
handle = open(name, 'r')
s = 0
x = re.findall(r'[0-9]+', handle.read())
for i in x :
    y = int(i)
    s = s + y
print(s)
