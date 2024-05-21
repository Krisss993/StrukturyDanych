
def insert_sort(lst):
    for sort_border in range(1,len(lst)):
        cur_idx = sort_border-1
        value = lst[cur_idx+1]

        while lst[cur_idx] > value and cur_idx >= 0:
            lst[cur_idx+1] = lst[cur_idx]
            cur_idx = cur_idx -1
        lst[cur_idx+1] = value
    print(lst)






insert_sort([4,7,2,7,231,87,32167,32,5467,324,12,43,51,655])
insert_sort([1,3,9,2,0,6,4,7,5,3])



