def calculate_bill(units):
    bill = 0

    if units > 300:
        bill += 100 * 3
        bill += 100 * 5
        bill += (units - 200) * 8
        bill += bill * 0.10  
    elif units > 200:
        bill += 100 * 3
        bill += 100 * 5
        bill += (units - 200) * 8
    elif units > 100:
        bill += 100 * 3
        bill += (units - 100) * 5
    else:
        bill += units * 3

    return int(bill)


units = int(input("Enter the unit"))
print(calculate_bill(units))
