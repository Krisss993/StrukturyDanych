# LISTY DWUKIERUNKOWE


microbiology = {
    'hour':9,
    'tname':'Wirus',
    'course':'microbiology',
    'prev':None,
    'next':None

}

chemistry = {
    'hour':12,
    'tname':'Kolba',
    'course':'chemistry',
    'prev':None,
    'next':None

}

ethics = {
    'hour':14,
    'tname':'Ojej',
    'course':'ethics',
    'prev':None,
    'next':None

}

microbiology['next']=chemistry
microbiology['prev']=None
chemistry['next']=ethics
chemistry['prev']=microbiology
ethics['next']=None
ethics['prev']=chemistry


print(ethics)

item = microbiology
while item:
    print(item['tname'])
    item = item['next']


def add_item_begin(my_collection, new_item):
    new_item['next'] = my_collection
    new_item['prev'] = None

    if my_collection:
        my_collection['prev'] = new_item

    my_collection = new_item
    return my_collection



def add_item_end(my_collection, new_item):
    if my_collection==None:
        my_collection = new_item
        new_item['prev'] = None
        new_item['next'] = None
        return my_collection
    else:
        item = my_collection
        while item['next']:
            item=item['next']
        item['next'] = new_item
        new_item['next']=None
        new_item['prev']=item
        return my_collection
