
l = [1,2,3,4,5,2]

i = l.__iter__()
print(i)
print(i.__next__())
print(i.__next__())
print(i.__next__())

print(list(map(lambda x:x**2, l)))
print([(lambda x:x**2)(a) for a in l])
print([x**2 for x in l])

print(list(filter(lambda x:x>=5,l)))

from functools import reduce

print(reduce(lambda x,y:x if x>y else y, l))

ids = ['id1','id200','id3']

print(sorted(ids, key=lambda x:int(x[2:])))


from heapq import nlargest, nsmallest

print(nsmallest(2,ids,key=lambda x:int(x[2:])))
print(nsmallest(2,ids))

l = [1, 45, 672, 7265, 16]

print(sorted(l, key=lambda i:str(i)[-1]))

codes = ['JPID', 'JJJPPP', 'XXX', 'JDU']

print(reduce(lambda x,y :x if len(x) < len(y) else y, codes))

capitals =['Rome', 'Paris', 'Madrid']
cities = ['Rome', 'Napoli', 'Rimini', 'Paris', 'Barcelona', 'Madrid', 'Marceille']

print(list(filter(lambda x:x not in capitals, cities)))




