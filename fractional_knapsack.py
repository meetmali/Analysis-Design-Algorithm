class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def fractionalKnapsack(W, arr):
    # Sorting Item on basis of ratio
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True)

    # Result(value in Knapsack)
    finalvalue = 0.0

    # Looping through all Items
    for item in arr:

        # If adding Item won't overflow,
        # add it completely
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.value

        else:
            finalvalue += item.value * W / item.weight
            break

    return finalvalue


if __name__ == "__main__":

    W = 20
    arr = [Item(21, 7), Item(24, 4), Item(12, 6), Item(40, 5), Item(30, 6)]

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(max_val)
