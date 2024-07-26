# pip install ydata-profiling

import pandas as pd 
import os 
from pathlib import Path 

from ydata_profiling import ProfileReport


os.chdir(Path(__file__).parent)


# 1. Read the csv file
df = pd.read_csv("./my_data.csv")


# 2. Create Profile
profile =  ProfileReport(df)


# 3. Save the profile 
profile.to_file(output_file= "./profile.html")

print("Saved successfully !")

