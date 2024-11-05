import numpy as np

# introduces what the program is and what is going to do
print("This is a program for calculatig the position of an objet in free fall based on the gravity and given hight, please introduce the following:")

# Asks the user for the seconds the program is going to calculate the position for
s = int(input("how many secons do you want to calculate the position for? ->"))

# Generate an array of time values from 1 to s (inclusive) with s number of elements
t = np.linspace(start=1, stop=s, num=s)

# Asks the user for the initial heigth position and the acceleration of gravity
h = float(input("introduce the heigth position please: "))
g = float(input("introduce the acceleraion of gravity please (Earths gravity is 9.8):"))


# calculate the position
print(f"calculating objet position for each second for {s} seconds")
print("...")

# function
y = h - 0.5*g*(t**2)

# Plot the results
print(y)