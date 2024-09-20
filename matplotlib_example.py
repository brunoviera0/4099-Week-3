import matplotlib.pyplot as plt  
import numpy as np  

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)  # Create an array of values t from 0 to 2 , with a step size of 0.01
s = 1 + np.sin(2 * np.pi * t)  # Calculate the s values (sin(2*pi*t)) and add 1 to shift the curve vertically

fig, ax = plt.subplots()  # Create a figure and a set of subplots (returns a figure and axis object)
ax.plot(t, s)  # Plot the time values 't' on the x-axis and the sine values 's' on the y-axis

# Set axis labels and title
ax.set(xlabel='x-axis', ylabel='y-axis', title='Simple Plot Example')  # Label the x-axis, y-axis, and set a title for the plot
ax.grid()  # Add a grid to the plot for better visual reference

fig.savefig("test.png")  # Save the figure to a file named "test.png"
plt.show()  # Display the plot window to the user
