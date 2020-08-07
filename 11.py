import re

lin = 'From olzhas.sutemgenov@nu.edu.kz Sat Jan 111 222 :222'
y = re.findall('^From \S+@(\S+)', lin)
print(y)
