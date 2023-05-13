nums = [12, 1, 3, 19, 22, 10, 8, 7, 6, 2]
elem_to_be_searched = 6

for elem in nums:
    if elem_to_be_searched == elem:
        print(f"The element's position is {nums.index(elem)}")
