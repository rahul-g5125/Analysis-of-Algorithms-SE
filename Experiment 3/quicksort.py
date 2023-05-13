def partition(a, low, high):
    pivot = a[low]
    start = low
    end = high

    while start <= end:
        while a[start] <= pivot:
            start += 1
        while a[end] > pivot:
            end -= 1
        if start < end:
            temp = a[start]
            a[start] = a[end]
            a[end] = temp
        temp2 = a[low]
        a[low] = a[end]
        a[end] = temp2
    return end


def quicksort(a, low, high):
    if low < high:
        j = partition(a, low, high)
        quicksort(a, low, j - 1)
        quicksort(a, j + 1, high)


L = [12, 1, 3, 19, 22, 10, 8, 7, 6, 2]
print(f"Before sorted: {L}")
quicksort(L, 0, 9)

print(f"The sorted array is {L}")
