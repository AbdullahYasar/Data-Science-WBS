import os
from pathlib import Path
import pandas as pd
from pprint import pprint
from sklearn.datasets import load_wine

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


os.chdir(Path(__file__).parent)


def raw_data():
    data = load_wine()
    print(dir(data))
    print(data['target_names'])

    return data


def show_dataframe():
    data = raw_data()

    # print(dir(data))
    # print(data['target_names'])

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    data = pd.DataFrame(data=data['data'],columns=data['feature_names'])
    # print(data.shape)
    # print(data.head())
    data.info()  #  178 entries
    data.describe() # All columns are 178 non-null  veriable. that means there
                    # isn't any missing value. And all column's type are float64
    return data 

def profiling_data():

    data = show_dataframe()
    
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
    # return data_statistic

# profiling_data()

class CModels:
    def __init__(self) -> None:
        self.data = raw_data()
        self.model1 = LogisticRegression()
        self.model2 = DecisionTreeClassifier() 

    def prepare_data(self):
        X_train, X_test, y_train, y_test = train_test_split(
            self.data.data, self.data.target, test_size = 0.2)

        return X_train, X_test, y_train, y_test


    def log_reg(self):
        
        X_train, X_test, y_train, y_test = self.prepare_data()

        self.model1.fit(X_train, y_train)

        print(self.model1.score(X_test, y_test))

        return self.model1.score(X_test, y_test)


    def des_tree(self):
        X_train, X_test, y_train, y_test = self.prepare_data()

        print(self.model2.fit(X_train, y_train))

        return self.model2.score(X_test, y_test)



models_= CModels()
print(models_.des_tree())

def cross_val():
    pass


def grid_search():
    pass


def save_models():
    pass


def results_storage():
    pass









# log_reg_model()

