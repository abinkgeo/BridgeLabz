def overflow_minute(inflows):
    capacity = 1000
    total = 0
    for i in range(len(inflows)):
        total += inflows[i]
        if total > capacity:
            return i + 1

N = int(input())
inflows = list(map(int, input("Enter the inflow").split()))
print(overflow_minute(inflows))
