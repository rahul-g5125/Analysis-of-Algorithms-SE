

def selection_sort(array):
    for i in range(len(array)):
        mini = i
        for j in range(i+1, len(array)):
            if array[j] < array[mini]:
                mini = j
        (array[i], array[mini]) = (array[mini], array[i])

    return array


L = []

# selected sort
print("Enter 10 numbers to sort")
for i in range(0, 10):
    num = int(input())
    L.append(num)

print(f"The sorted array is {selection_sort(L)}")
# 100 12 14 15 18 21 19 22 32 10