def search_binary(lst, value):
    start = 0
    end = len(lst) - 1
    found = False

    while start <= end and value >= lst[start] and value <= lst[end]:
        print(f'DEBUG {start} - {end}')
        if lst[start] != lst[end]:
            mid = start + int( (float(end-start) / (lst[end] - lst[start])) * (value - lst[start]) )
        else:
            mid=start
        if lst[mid] == value:
            found=True
            break
        else:
            if value < lst[mid]:
                end = mid-1
            else:
                start = mid+1
    if found:
        return mid
    else:
        return None

print(search_binary([2, 4, 7, 7, 12, 32, 43, 51, 87, 231, 324, 655, 5467, 32167], 231))

