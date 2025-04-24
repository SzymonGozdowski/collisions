import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


# Function to calculate post-collision velocity (elastic collision)
def calculate_velocity(m1, m2, v1, v2):
    v1_final = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2_final = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return v1_final, v2_final


# Initialize values
x1, y1 = 1, 4  # Position of ball 1
x2, y2 = 20, 4  # Position of ball 2
x3, y3 = 0, 4
vel1, vel2, vel3 = 5, -1, 2  # Initial velocities
m1, m2, m3 = 1, 30, 30  # Masses (equal)

# Set up figure
fig, ax = plt.subplots()
ax.set_xlim(0, 25)
ax.set_ylim(3, 5)

# Create scatter plot for two balls
ball1 = ax.scatter(x1, y1, color="red", s=100)   # Red ball
ball2 = ax.scatter(x2, y2, color="blue", s=100)  # Blue ball
ball3 = ax.scatter(x3, y3, color="green", s=100)  # Green ball


# Function to update positions for animation
def update(frame):
    global x1, x2, x3, vel1, vel2, vel3
    dt = 0.05  # Small-time step

    # Check for collision
    if abs(x1 - x2) <= 0.3:  # Simple collision condition
        vel1, vel2 = calculate_velocity(m1, m2, vel1, vel2)
    if abs(x1 - x3) <= 0.3:
        vel1, vel3 = calculate_velocity(m1, m3, vel1, vel3)
    # Update positions
    x1 += vel1 * dt
    x2 += vel2 * dt
    x3 += vel3 * dt

    # Update scatter plot positions
    ball1.set_offsets([x1, y1])
    ball2.set_offsets([x2, y2])
    ball3.set_offsets([x3, y3])
    return ball1, ball2, ball3


# Run animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=20, blit=True)
plt.show()
