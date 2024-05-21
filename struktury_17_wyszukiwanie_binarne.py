def divide(lst, start, end):
    i = start
    border_value = lst[end]
    for j in range(start, end):
        if lst[j] < border_value:
            lst[j], lst[i] = lst[i], lst[j]
            i+=1
    lst[end], lst[i] = lst[i], lst[end]
    return i
def q_sort(lst, start, end):
    if start < end:
        border_index = divide(lst, start, end)
        q_sort(lst, start, border_index - 1)
        q_sort(lst, border_index + 1, end)
    return lst

lst = [4,7,2,7,231,87,32167,32,5467,324,12,43,51,655]
q_sort(lst, 0, len(lst) - 1)

sorted_lst = q_sort(lst, 0, len(lst) - 1)
print(sorted_lst)
def search_binary(lst, value):
    start = 0
    end = len(lst) - 1
    found = False
    while start <= end and not found:
        print(f'DEBUG {start} - {end}')
        mid = (start+end) // 2
        if lst[mid] == value:
            found=True
        else:
            if value < lst[mid]:
                end = mid-1
            else:
                start = mid+1
    if found:
        return mid
    else:
        return None

print(search_binary(sorted_lst, 32))

