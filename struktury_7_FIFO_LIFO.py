
list_fifo = []
list_fifo.append('str1')
list_fifo.append('str2')
list_fifo.append('str3')


for i in range(len(list_fifo)):
    task = list_fifo.pop(0)
    print(task)


list_lifo = []

list_lifo.append('Blue Box with Glass')
list_lifo.append('Bag with Presents')
list_lifo.append('Barrel of Beer')
list_lifo.append('Cage with a Tiger')

print(list_lifo)

for i in range(len(list_lifo)):
    print(list_lifo.pop())

print(list_lifo)
