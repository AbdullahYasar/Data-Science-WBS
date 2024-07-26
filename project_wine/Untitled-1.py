#%%
import os
from pathlib import Path
import pandas as pd
from sklearn.datasets import load_wine
from pprint import pprint
import matplotlib.pyplot as plt 


data = load_wine()
# print(dir(data))
# print(data['target_names'])

pd.set_option("display.max_rows", None, "display.max_columns", None)
data = pd.DataFrame(data=data['data'],columns=data['feature_names'])


statistic_of_data ={}
for column in data:
    my_dict = {}
    Mean = data[column].mean()
    median = data[column].median()
    range_ = data[column].max() - data[column].min()
    std_dev =  data[column].std()

    my_dict = {"Mean" :  Mean ,
                        "median ": median,
                        "range_ ": range_,
                        "standart deviation" : std_dev}

    statistic_of_data[column] = my_dict 

data_statistic = pd.DataFrame(statistic_of_data)
print(data_statistic)
                                
#pprint(statistic_of_data )     

    # print(column)
    # print("Mean :" , Mean)
    # print("median :" , median)
    # print("range_ :" , range_)
    # print("standart deviation :" , std_dev)
    # print("*"*20)
        
    #%%
    # column = "özellik"

    # baslik = "1.sütun"

    # diction_ = {}
    # üst_szlk = {}
    # med = 6
    # mean = 8

    
    # diction_[column] = med
    # diction_['asda'] = mean
    # üst_szlk[baslik] = diction_    

    # print(üst_szlk)

#%%


plt.scatter(data["proline"], data["alcalinity_of_ash"])
plt.show()




