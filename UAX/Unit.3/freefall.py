a = float(input("Acceleration (on earth 9,8): "))
x = float(input("Height: "))
v = float(input("Starting velocity: "))
t = float(input("Time passed: "))

# Here I use the ecuation to calculate position in freefall
print(f"The final position is: {x+v*t-0.5*a*t**2} meters high at {t} seconds")