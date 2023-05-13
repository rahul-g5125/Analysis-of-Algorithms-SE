def divide_minmax(a, low, high):
    maxi = a[low]
    mini = a[low]

    if low == high:
        mini = a[low]
        maxi = a[low]
        return maxi, mini
    elif low + 1 == high:
        if a[low] > a[high]:
            maxi = a[low]
            mini = a[high]
        else:
            maxi = a[high]
            mini = a[low]
        return maxi, mini
    else:
        mid = int((low+high)/2)
        mL = divide_minmax(a, low, mid)
        mR = divide_minmax(a, mid+1, high)
        return max(mL[0], mL[0]), min(mL[1], mR[1])

arr = [12, 1, 3, 19, 22, 10, 8, 7, 6, 2]
h = len(arr) - 1
l = 0

result = divide_minmax(arr, l, h)
print(f"Minimum of {arr} is {result[0]}")
print(f"Maximum of {arr} is {result[1]}")
