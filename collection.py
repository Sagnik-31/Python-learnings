# collections: counter, namedtuple, DefaultDict, deque

from collections import Counter, defaultdict, deque, namedtuple
a = "aaabbc"
c = ['a','a','b','c','c']
print(Counter(c)) # .items() , .keys(), values()
print(Counter(a))

my_c = Counter(a)
print(my_c.most_common(1)[0][0])

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c']) # output 0 for missing key

Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt.x, pt.y)

dd = deque()
dd.append(1)
dd.append(2)
print(dd)
dd.popleft() # .rotate(1) , .extend([4,5,6])
print(dd)


