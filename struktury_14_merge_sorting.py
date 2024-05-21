def merge_sort(lst):
    list_len = len(lst)
    sorted_list = []

    if list_len <=1:
        sorted_list = lst
    else:
        middle_point = list_len // 2
        list_left = merge_sort(lst[:middle_point])
        list_right = merge_sort(lst[middle_point:])

        idx_left =  0
        idx_right = 0
        while idx_left < len(list_left) and idx_right < len(list_right):
            if list_left[idx_left] < list_right[idx_right]:
                sorted_list.append(list_left[idx_left])
                idx_left+=1
            else:
                sorted_list.append(list_right[idx_right])
                idx_right+=1

        sorted_list.extend(list_left[idx_left:])
        sorted_list.extend(list_right[idx_right:])

    print(f'DEBUG: {lst} --> {sorted_list}')

    return sorted_list

merge_sort([4,7,2,7,231,87,32167,32,5467,324,12,43,51,655])
merge_sort([1,3,9,2,0,6,4,7,5,3])
merge_sort([1,5,3,9])

