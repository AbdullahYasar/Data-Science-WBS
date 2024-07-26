"""Generate a Report manually (without reporting libraries) about an input csv file using pandas.
input file : "my_data.csv"
How many columns ? and data types?
How many rows ?
How many NAN Values ?
How many duplicated rows?
The output file "report.txt" should saved"""


import pandas as pd
import numpy as np


df = pd.read_csv("./my_data.csv")


class Report1:

    def info_cl_rw(self):

        rows = data1.shape[0]
        print(f"{data1} have {rows} rows")
        columns = data1.shape[1]
        print(f"{data1} have {columns} columns")





