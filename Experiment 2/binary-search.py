nums = [12, 1, 3, 19, 22, 10, 8, 7, 6, 2]
elem_to_be_searched = 6

sorted_nums = sorted(nums)
print(f"The element to be searched is {elem_to_be_searched} from {sorted_nums}.")
def rec_binary_search(array, low, high, element):
    if low == high:
        if array[low] == element:
            return low
        else:
            return -1
    else:
        mid = int((low + high)/2)
        if element == array[mid]:
            return mid
        elif element < array[mid]:
            return rec_binary_search(array, low, mid-1, element)
        elif element > array[mid]:
            return rec_binary_search(array, mid+1, high, element)

print(f"It is at position {rec_binary_search(sorted_nums, 0, 9, elem_to_be_searched)+1}")

# def non_rec_binary_search(array, low, high, element):
#     mid = 0
#     while low <= high:
#         mid = int((low + high)/2)
#         if element == array[mid]:
#             break
#         elif element < array[mid]:
#             high = mid - 1
#         elif element > array[mid]:
#             low = mid + 1
#     if low <= high:
#         return mid
#     else:
#         return -1
#
# print(f"Answer by non-recursive binary search: {non_rec_binary_search(sorted_nums, 0, 9, elem_to_be_searched)}")
