
# pip install matplotlib

import os 
from pathlib import Path 
from matplotlib import pyplot as plt 

os.chdir(Path(__file__).parent)

# Data
x = [1,2,3,4,5,6,6]
y = [10, 29, 30, 43, 51,65, 71]

fig, ax = plt.subplots(2, 2)


# Format: Row , Column
#~~~~~~~~~~~~~~~~~~~~~

# Row: 0
##########
ax[0, 0].plot(x, y, color = "green")
ax[0, 1].plot(x, y, color = "red")



# Row: 1
##########
ax[1, 0].plot(x, y, color = "blue")
ax[1, 1].plot(x, y, color = "black")



# Show plot
plt.show()