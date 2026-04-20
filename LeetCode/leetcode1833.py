
def maxIceCream(costs, coins):
    # Step 1: Counting Sort - O(n + max_cost)
    max_val = max(costs)
    count = [0] * (max_val + 1)

    # Count frequency of each cost
    for cost in costs:
        count[cost] += 1

    # Step 2: Greedy - buy cheapest first
    ice_creams = 0
    for cost in range(len(count)):
        if coins <= 0:
            break
        if count[cost] > 0:
            # How many of this cost can we afford?
            can_buy = min(count[cost], coins // cost)
            ice_creams += can_buy
            coins -= can_buy * cost

    return ice_creams
        
costs = [1,6,3,1,2,5]
coins = 20
print(maxIceCream(costs, coins))