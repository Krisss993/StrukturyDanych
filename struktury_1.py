

ben = {
    'name':'Ben',
    'phone':821233,
    'email':'ma@wp.pl'
}

jan = {
    'name':'Jan',
    'phone':965423,
    'email':'aa@wp.pl'
}
ann = {
    'name':'Ann',
    'phone':42433,
    'email':'wg@wp.pl'
}

contacts = [ben, jan, ann]
print(contacts)

emails = ';'.join([dic['email'] for dic in contacts])
print(emails)

emails = []
for dic in contacts:
    emails.append(dic['email'])
print(emails)

d = {}
for k in contacts[0].keys():
    d[k] = []
for di in contacts:
    for k, v in di.items():
        d[k].append(v)
print(d)


d = {}
for di in contacts:
    print(di)
    print(di['name'])
    d[di['name']] = di
print(d)

print(d['Ben']['email'])

microbiology = {
    'hour':9,
    'tname':'Wirus',
    'course':'microbiology'
}

chemistry = {
    'hour':12,
    'tname':'Kolba',
    'course':'chemistry'
}

ethics = {
    'hour':14,
    'tname':'Ojej',
    'course':'ethics'
}

lab1 = [microbiology, chemistry, ethics]
print(lab1)

print()
print()

lab2 = {}

for dic in lab1:
    lab2[dic['course']]=dic

print(lab2)

for dic in lab1:
    print(dic['tname'])

for k, v in lab2.items():
    print(v['tname'])

