def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


L = []
print("Enter 5 numbers to sort")

for i in range(0, 5):
    num = int(input())
    L.append(num)

insertion_sort(L)

print(f"The sorted array is {L}")
