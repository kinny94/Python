# Counter - It counts

from collections import Counter
l = [1,1,1,1,1,3,3,3,4,5,5,5,5,5,6,6,6,7]
print Counter(l)

s = "Mydsadadadadasdadadassdadaw"
words = s.split()
print Counter(words)

c = Counter(words)
print c.most_common(3)

# other important sum(c.values())
#c.clear()
#list(c)
#set(c)
#dict(c)

# Default Dict
from collections import defaultdict
d = {'k1' : 1}
try:
	print ['k2']
except: 
	print "Intentional Error cause K2 do not exists"

x = defaultdict(object)
print x

#Order Dict
d2 = {}
d2['a'] = 1
d2['b'] = 2
d2['c'] = 3

for k,v in d2.items():
	print k,v

from collections import orderdict
d2 = orderdict
d2['a'] = 1
d2['b'] = 2
d2['c'] = 3
for k,v in d2.items():
	print  k,v

#Date Time
import datetime
t = datetime(5,23,31)
print t
print t.hour
print t.minute
print t.seconds

today = datetime.date.today()
print today