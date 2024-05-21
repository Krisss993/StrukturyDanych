wi1 = {
    "name" : "Clean room A",
    "prev" : None,
    "next" : None
}
wi2 = {
    "name" : "Clean room B",
    "prev" : None,
    "next" : None
}
wi3 = {
    "name" : "Clean room C",
    "prev" : None,
    "next" : None
}

# wi1['next'] = wi2
# wi2['prev'] = wi1
# wi2['next'] = wi3
# wi3['prev'] = wi2

head = wi1

def add_item_begin(collection, new_item):
    if collection is None:
        collection = new_item

        return collection
    else:
        collection['prev'] = new_item
        new_item['next'] = collection
    return collection



def add_item_end(collection, new_item):
    if collection is None:
        collection = new_item
        print(collection)
        return collection
    else:
        current = collection
        while current['next']:
            current = current['next']
        current['next'] = new_item
        new_item['prev'] = current
        return collection

wi0 = {
    "name" : "Clean room 0",
    "prev" : None,
    "next" : None
}
wi4 = {
    "name" : "Clean room 4",
    "prev" : None,
    "next" : None
}

# add_item_begin(head,wi0)
#
# print(wi1['prev'])
#
# add_item_end(head, wi4)
#
# print(wi4['prev'])
# print(wi4['next'])
# print(wi3['next'])
#
# print()
# print()
# print()
# print()

work = None
add_item_end(work, wi1)
add_item_end(work, wi2)
add_item_end(work, wi3)
print(work)

item = work
while item:
    print(item['name'])
    item = item['next']




def add_at_start(data, new_node):
    new_node['next'] = data
    new_node['prev'] = None
    if data:
        data['prev'] = new_node
    data = new_node
    return data

def add_at_end(data, new_node):
    if data is None:
        new_node = data
        new_node['next'] = None
        new_node['prev'] = None
    else:
        item = data
        while item['next']:
            item = item['next']
        item['next'] = new_node
        new_node['next'] = None
        new_node['prev'] = item
    return data

def del_at_begin(data):
    if data:
        item = data
        while item['prev']:
            item = item['prev']
        data = item['next']
        data['prev'] = None
        item['next'] = None
    return data

add_at_start(wi2,wi1)
print(wi2['prev'])
print(wi1['next'])
del_at_begin(wi2)
print(wi2['prev'])
print(wi1['next'])

def del_at_end(data):
    if data:
        item = data
        while item['next']:
            item = item['next']
        data = item['prev']
        data['next'] = None
        item['prev'] = None
    return data