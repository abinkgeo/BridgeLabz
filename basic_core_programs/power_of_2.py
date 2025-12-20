print("Enter values less than 32")
N =int(input("Enter the value of N"))
if(N<=31):
    for i in range(1,N+1):
        print(f"2 ^ {i} = {2**i}")

else:
    print("Enter values less than 32")