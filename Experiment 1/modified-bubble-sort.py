L = []
i = 0
# modified-bubble sort
print("Enter 10 numbers to sort")
for i in range(0, 10):
    num = int(input())
    L.append(num)

flag = 1

while flag == 1 and i <= len(L)-1:
    for j in range(0, len(L)-i-1):
        if L[j] > L[j+1]:
            temp = L[j]
            L[j] = L[j+1]
            L[j+1] = temp
            flag = 1

print(f"The sorted array is {L}")
