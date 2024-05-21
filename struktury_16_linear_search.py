def linear_search(lst, value):
    res = []
    idxs= []
    idx = -1
    for nr in lst:
        idx +=1
        if nr == value:
            res.append(nr)
            idxs.append(idx)
            # break
    return (res, idxs) if len(res) > 0 else None

print(linear_search([3,5,743,23,6,3,6,44,56,22,6552,],22))
print(linear_search([3,5,743,23,6,3,6,44,56,22,6552,],224))

def linear_search2(lst, value):
    idx = 0
    found = False
    while not found and idx < len(lst):
        if lst[idx] == value:
            found=True
        else:
            idx+=1
    return idx if idx < len(lst) else None



print(linear_search2([3,5,743,23,6,3,6,44,56,22,6552,],22))
print(linear_search2([3,5,743,23,6,3,6,44,56,22,6552,],224))
