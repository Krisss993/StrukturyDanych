import queue

q = queue.Queue()

for i in range(11,16):
    q.put(i)
print(q.qsize())

while q.qsize() > 0:
    print(f'Getting: {q.get()}, the que size is {q.qsize()}')


lifo = queue.LifoQueue()
for i in range(11,16):
    lifo.put(i)
print(lifo.qsize())

while lifo.qsize() > 0:
    print(f'Getting: {lifo.get()}, the que size is {lifo.qsize()}')

prior = queue.PriorityQueue()
prior.put((1, 'task1'))
prior.put((3, 'task3'))
prior.put((2, 'task2'))
prior.put((1, 'task1 - again'))
while prior.qsize() > 0:
    print(f'Getting: {prior.get()}, the que size is {prior.qsize()}')

