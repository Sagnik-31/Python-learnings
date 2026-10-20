# itertools
# product, permutations, combinations, accumulate, groupby, infinite iterators
import operator
from itertools import product, permutations, combinations, accumulate, groupby, combinations_with_replacement
#product -> cartesian product
a = [1,2]
b = [3,4]
prod = product(a,b, repeat=1)
print(list(prod))

#permutations
c = [1,2,3]
perm = permutations(c,3)
print(list(perm))

#combinations
d = [1,2,3,4]
comb = combinations(d,2) # 4C2
comb_wr = combinations_with_replacement(d,2)
print(list(comb))
print(list(comb_wr))

# accumulate
acc = accumulate(d, func=operator.add)
print(d)
print(list(acc))

#group by
e = [1,2,3,4]
group_obj = groupby(e, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value))
