
# pip install matplotlib

import os 
from pathlib import Path 
from matplotlib import pyplot as plt 

os.chdir(Path(__file__).parent)

# Data
x = [1,2,3,4,5,6,6]
y = [10, 29, 30, 43, 51,65, 71]


plt.subplot(2, 2, 1)
plt.plot(x, y, color = "blue")



plt.subplot(2, 2, 2)
plt.plot(x, y, color = "green")


plt.subplot(2, 2, 3)
plt.plot(x, y, color = "red")



plt.subplot(2, 2, 4)
plt.plot(x, y, color = "black")




plt.figure(figsize=(10,6))


# Show the plot
plt.show()