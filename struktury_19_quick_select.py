def divide(lst, start, end):
    i = start
    border_value = lst[end]
    for j in range(start,end):
        if lst[j] < border_value:
            lst[i], lst[j] = lst[j], lst[i]
            i+=1
    lst[end], lst[i] = lst[i], lst[end]
    return i



def quick_select(lst, start, end, k_th):

    print(f'DEBUG: {lst}')
    if k_th >= len(lst):
        return None

    if start <= end:
        border_index = divide(lst, start, end)
        if border_index == k_th:
            return lst[border_index]
        elif border_index > k_th:
            return quick_select(lst, start, border_index-1, k_th)
        else:
            return quick_select(lst, border_index+1, end, k_th)

lst = [4,7,2,7,231,87,32167,32,5467,324,12,43,51,655]
print(quick_select(lst,0, len(lst)-1, 4))

