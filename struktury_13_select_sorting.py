

def insert_sort(lst):
    for border in range(1,len(lst)):
        curr_idx = border-1
        value = lst[curr_idx+1]

        while lst[curr_idx] > value and curr_idx >= 0:
            lst[curr_idx+1] = lst[curr_idx]
            curr_idx = curr_idx-1
        lst[curr_idx+1] = value
    print(lst)




insert_sort([4,7,2,7,231,87,32167,32,5467,324,12,43,51,655])
insert_sort([1,3,9,2,0,6,4,7,5,3])




def select_sorting(lst):
    for run in range(len(lst)):
        min_index = run
        for i in range(run+1, len(lst)):
            if lst[i] < lst[min_index]:
                min_index = i
        lst[run], lst[min_index] = lst[min_index], lst[run]


def select_sorting(lst):
    for r in range(len(lst)):
        min_idx = r
        for i in range(r+1, len(lst)):
            if lst[i] < lst[min_idx]:
                min_idx = i
        lst[r], lst[min_idx] = lst[min_idx], lst[r]
    print(lst)


select_sorting([4,7,2,7,231,87,32167,32,5467,324,12,43,51,655])
select_sorting([1,3,9,2,0,6,4,7,5,3])

def bubble_sort(lst):
    for max_NSI in range(len(lst)-1,0,-1):
        is_change=False
        for i in range(max_NSI):
            if lst[i+1] < lst[i]:
                lst[i+1], lst[i] = lst[i],lst[i+1]
                is_change=True
        if not is_change:
            break
    print(lst)


bubble_sort([4,7,2,7,231,87,32167,32,5467,324,12,43,51,655])
bubble_sort([1,3,9,2,0,6,4,7,5,3])
