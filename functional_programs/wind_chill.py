import math

t=float(input("Enter the temparature in Fahrenheit(absolute(t)<=50): "))
v=float(input("Enter the windspeed in mph(3<=v<=120) : "))

if(abs(t)<=50 and (v>=3 and v<=120)):
   
    wind_chill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
    print(f"Wind Chill {wind_chill:.2f}")

else:
    print("Invalid Input")