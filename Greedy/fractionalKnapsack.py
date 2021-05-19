def fractionalKnapsack(items, weight):
    max = 0
    r_weight = weight
    for i in range(len(items)):
        items[i].append((items[i][0]/items[i][1]))
    items.sort(reverse=True, key=lambda x: x[2])
    for i in range(len(items)):
        if r_weight == 0:
            break
        if items[i][1]<=r_weight :
            max += items[i][0]
            r_weight = r_weight - items[i][1]
        else:
            max += items[i][0]* (r_weight/items[i][1])
            r_weight = 0

    return max





items = []
weight = int(input("Enter the Knapsack Capacity: "))
n = int(input("Enter the number of items: "))
print("Enter the value prooceeded by weight of item")
for i in range(n):
    item = list(map(int, input().split()))
    items.append(item)

print("Maximum Possible Value in Knapsack is: ",fractionalKnapsack(items, weight))