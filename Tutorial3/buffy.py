import numpy as np

# x, y
position = np.array([0.0, 0.0]) # m
velocity = np.array([4.4, 4.4]) # m/s
gravity = np.array([0.0, -9.8]) # m/s^2

floorPosition = -1.24

time = 0.0
dTime = 0.01 #s

dragCoefficient = 0.05 #m^-1

while position[1] >= floorPosition:
    acceleration = gravity - dragCoefficient * velocity * np.linalg.norm(velocity)

    position += dTime * velocity
    velocity += dTime * acceleration

    time += dTime

print(position)
print(round(time, 2))
