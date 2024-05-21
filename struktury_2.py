my_list = [1,5,23,7,3,2]

def sq(x):
    return x**2

print([sq(x) for x in my_list])

print([(lambda x:x**2)(a) for a in my_list])
print([(lambda x:x**2)(x) for x in my_list])

names = ['John Johnson', 'Alicja Policja', 'Wladimir Wladymirowicz']

def get_sub_name(name, part):
    return [x.split(' ')[part] for x in name]

print(get_sub_name(names,0))
print(get_sub_name(names,1))

def get_sub_name(name, part):
    res = []
    for x in name:
        res.append(x.split(' ')[part])
    return res

print(get_sub_name(names,0))
print(get_sub_name(names,1))

def get_sub_name(name, part):
    name = name.split(' ')
    return name[part]

print([get_sub_name(x,0) for x in names])

print([(lambda x:x.split(' ')[0])(a) for a in names])
