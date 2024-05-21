

def quick_sort_divide(list, start, end):
     i = start
     border_value = list[end]
     for j in range(start, end):
         if list[j] <= border_value:
             list[i], list[j] = list[j], list[i]
             i += 1
     list[i], list[end] = list[end], list[i]
     print(list)
     return i



def quick_sort(lst, start, end):
     if start < end:
         border_index = quick_sort_divide(lst, start, end)
         quick_sort(lst, start, border_index -1)
         quick_sort(lst, border_index + 1, end)


lst = [4,7,2,7,231,87,32167,32,5467,324,12,43,51,655]
quick_sort(lst,0, len(lst)-1)
# quick_sort([1,3,9,2,0,6,4,7,5,3])
# quick_sort([1,5,3,9])
