L = []

# bubble sort
print("Enter 5 numbers to sort")
for i in range(0, 5):
    num = int(input())
    L.append(num)

for j in range(0, len(L)-2):
    for i in range(0, len(L)-j-1):
        if L[i] > L[i+1]:
            temp = L[i]
            L[i] = L[i+1]
            L[i+1] = temp

print(f"The sorted array is {L}")
