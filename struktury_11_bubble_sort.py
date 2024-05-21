
def bubble_sord(lst):
    is_change = True
    while is_change:
        is_change = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_change = True
    print(lst)

bubble_sord([4,7,2,7,231,87,32167,32,5467,324,12,43,51,655])
bubble_sord([1,3,9,2,0,6,4,7,5,3])


def sort_bubble2(list):
     # don't compare values at the end of the list - they are already sorted
     max_index = len(list) - 1
     for max_i in range(max_index,0,-1):
         is_change = False
         for i in range(max_i):
             if list[i] > list[i+1]:
                 list[i],list[i+1] = list[i+1],list[i]
                 is_change = True

         if not is_change:
            break

sort_bubble2([4,7,2,7,231,87,32167,32,5467,324,12,43,51,655])
# # checking time - case sort_bubble
# start = time.time()
# sort_bubble(my_list1)
# stop = time.time()
# print(f'Sorting duration for function sort_bubble: {stop - start}')
# # checking time - case sort_bubble2
# start = time.time()
# sort_bubble2(my_list2)
# stop = time.time()
# print(f'Sorting duration for function sort_bubble2: {stop - start}')


