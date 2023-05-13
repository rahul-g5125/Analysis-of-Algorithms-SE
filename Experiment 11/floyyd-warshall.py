# n = int(input("What is the number of vertices?: "))
# print(f"Enter the graph matrix values for {n}x{n} matrix: ")
G = [[0, 3, 999, 5], [2, 0, 999, 4], [999, 1, 0, 999], [999, 999, 2, 0]]
n = len(G)
D = [[0 for i in range(n)] for j in range(n)]
S = [[0 for k in range(n)] for l in range(n)]


for i in range(n):
    for j in range(n):
        D[i][j] = G[i][j]
        if  i == j:
            S[i][j] = 999
        else:
            S[i][j] = j

for k in range(n):
    for i in range(n):
        for j in range(n):
            if D[i][k] + D[k][j] < D[i][j]:
                D[i][j] = D[i][k] +D[k][j]
                S[i][j] = k


for i in range(n):
    for j in range(i+1, n):
        if S[i][j] == j:
            print(f"Source: {i} Destination: {j} path: {i}->{j} distance:{D[i][j]}")
        else:
            k = S[i][j]
            print(f"Source: {i} Destination: {j} path: {i}->")
            while k != j:
                print(f"{k}->")
                k = S[k][j]
            print(f"{j} Distance: {D[i][j]}")

print(D)
print(S)