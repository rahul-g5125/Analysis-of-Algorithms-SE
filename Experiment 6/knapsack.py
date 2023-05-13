class Knapsack:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.ratio = profit/weight

    weights = []
    profits = []
    ratios = []


u = int(input("Enter the total capacity: "))

no_of_elements = int(input("How many elements need to be inserted?: "))
knapsacks = []


def give_ratio(knapsack):
    return knapsack.ratio


for i in range(no_of_elements):
    weight = int(input(f"Enter weight of knapsack {i+1}: "))
    profit = int(input(f"Enter profit of knapsack {i+1}: "))
    knapsacks.append(Knapsack(weight, profit))

sorted_knapsacks = sorted(knapsacks, key=give_ratio, reverse=True)

for i in range(no_of_elements):
    print(f"Weight, profit, ratio of sorted knapsacks: {sorted_knapsacks[i].weight}, {sorted_knapsacks[i].profit}, {sorted_knapsacks[i].ratio}")

i = 0
x = []
while u > 0:
    if sorted_knapsacks[i].weight <= u:
        x.append(1)
        u = u - sorted_knapsacks[i].weight
    else:
        x.append(u/sorted_knapsacks[i].weight)
    i += 1
    u = 0

total_profit = 0
for i in range(no_of_elements - 1):
    total_profit += sorted_knapsacks[i].profit

print("The ratios are ", x)
print("The total profit is ", total_profit)