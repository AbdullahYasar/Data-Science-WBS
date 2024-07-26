

# pip install matplotlib

import os 
from pathlib import Path 
from matplotlib import pyplot as plt 

os.chdir(Path(__file__).parent)

# Data
x = [1,2,3,4,5,6,6]
y = [10, 29, 30, 43, 51,65, 71]
price = [11,32,41,1,2,17,24]


# 1. Create a figure (Window)
fig = plt.figure() 

# 2. Create a draw area (subplot)
ax = fig.add_subplot(111)


# 3. Draw the graph/plot in the draw area
ax.plot(x, y, color = "green", linewidth = 5, linestyle = "--", label = "Market Dev")
ax.plot(x, price, color = "blue", linewidth = 5, linestyle = ":", label = "Revenue")


# Scatter
ax.scatter([2,3,4], [23,24,36] , marker = "^" , color = "red", s = 70 ) # s: size

# 4. Plot Configuration
plt.legend()
plt.grid(True)
plt.title("My first diagram")
plt.xlabel("Check Point")
plt.ylabel("Price")

# 5. Save the plot as an image
plt.savefig("./images/myfigure2.png")

# 6. Show the plot
plt.show()


