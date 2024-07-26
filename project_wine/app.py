import os
from pathlib import Path
import pandas as pd
from pprint import pprint
import numpy as np
from datetime import datetime
from sklearn.datasets import load_wine

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score 
from sklearn.model_selection import RepeatedStratifiedKFold 
from sklearn.model_selection import GridSearchCV


import seaborn as sn
import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split


os.chdir(Path(__file__).parent)


def raw_data():
    data = load_wine()

    return data


def show_dataframe():
    data = raw_data()

    # print(dir(data))
    # print(data['target_names'])

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    data = pd.DataFrame(data=data['data'],columns=data['feature_names'])
    # print(data.shape)
    # print(data.head())
    # data.info()  #  178 entries
    # data.describe() # All columns are 178 non-null  veriable. that means there
                    # isn't any missing value. And all column's type are float64
    return data 


def profiling_data():
    data = show_dataframe()
    datenow = datetime.now()

    statistic_of_data ={}
    my_dict = {}
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


    # statistic_of_data["Statistics"] = my_dict.keys()
    statistic_of_data["Date"] = datenow
    data_statistic = pd.DataFrame(statistic_of_data)
    
    print(data_statistic) 
    return data_statistic

#profiling_data()

def log_reg():
    data = raw_data()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size = 0.2)

    model = LogisticRegression(solver='liblinear')
    model.fit(X_train, y_train)

    print(model.score(X_test, y_test))

    return model.score(X_train, y_train)

# log_reg()

def des_tree():
    data = raw_data()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size = 0.2)

    model = DecisionTreeClassifier() 
    model.fit(X_train, y_train)

    print(model.score(X_test, y_test))

    return model.score(X_train, y_train)

# des_tree()

def ran_for():
    data = raw_data()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size = 0.2)

    model1 = RandomForestClassifier(n_estimators= 50,random_state=40) 
    model1.fit(X_train, y_train)
    
    model2 = RandomForestClassifier(n_estimators= 100,random_state=40) 
    model2.fit(X_train, y_train)
    
    model3 = RandomForestClassifier(n_estimators= 500,random_state=40) 
    model3.fit(X_train, y_train)

    print(model1.score(X_test, y_test))
    print(model2.score(X_test, y_test))
    print(model3.score(X_test, y_test))  # All scors are 1.0. Now we need to compare predic. and target to 
                                        # understand there is overfitting or not

    y_predicted = model1.predict(X_test) # model1 need to little time
    cm = confusion_matrix(y_test , y_predicted )  # with this result we saw there isn`t overfitting. evrtng is fine :)
    sn.heatmap(cm ,annot = True)
    plt.xlabel("Predicted")
    plt.ylabel("Truth")
    # plt.show()
    return model3.score(X_test, y_test)

# ran_for()

def knn():
    data = raw_data()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size = 0.2)
    
    model = KNeighborsClassifier(n_neighbors= 3)  # score 0.75, the best score 
    # model = KNeighborsClassifier(n_neighbors= 4) # score 0.6944444444444444
    # model = KNeighborsClassifier(n_neighbors= 5) # score 0.6666666666666666
    model.fit(X_train, y_train)


    print(model.score(X_test, y_test))
    return model.score(X_test, y_test)

# knn()

def cross_val():
    data = raw_data()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size = 0.2)
    
    k_fold = RepeatedStratifiedKFold(n_splits=5, n_repeats= 3 )
    scores_200 = cross_val_score(RandomForestClassifier(n_estimators= 200)  , data.data, data.target , cv = k_fold  )

    print("Average Score 200: ", np.average(scores_200))

    return np.average(scores_200)

#cross_val()
    
def grid_search():
    data = raw_data()
    cv = RepeatedStratifiedKFold(n_splits = 10 , n_repeats= 3)

    model_param_grid = {
        "logisitc_regression": {
            "model": LogisticRegression(),
            "param_grid": {
                            "solver": ["lbfgs" , "liblinear"],
                            "C" : [100, 10, 1.0, 0.1]
                        }
        },
        "randomforest": {
            "model": RandomForestClassifier(),
            "param_grid": {
                "n_estimators": [10, 50 , 100 ,500]
            }
        }
    }

    scores = []

    for model_name, model_param in model_param_grid.items():
        grid_search = GridSearchCV(estimator=model_param["model"] , param_grid= model_param["param_grid"], cv = cv)
        grid_search.fit(data.data, data.target)

        scores.append({
            "model": model_name,
            "best_score" : grid_search.best_score_,
            "best_param" : grid_search.best_params_,
        })

    df_multi_grid = pd.DataFrame(scores, columns= ["model", "best_score", "best_param"])
    return df_multi_grid
    #                  model  best_score                         best_param
    # 0  logisitc_regression    0.954902  {'C': 100, 'solver': 'liblinear'}
    # 1  randomforest           0.983224              {'n_estimators': 500}

#grid_search()

def save_models():
    pass

def results_storage():
    date = datetime.now()

    res1 = log_reg()
    res2 = des_tree()
    res3 = ran_for()
    res4 = knn()
    res5 = cross_val()

    df = pd.DataFrame({"Date" : date, "Logistic Regression " : res1, "Decision Tree Classifier" : res2,
                       "Random Forest Classifier" : res3, "KNeighbors Classifier" : res4,
                        " Cross-Validation" : res5 }, index = [0])
    
    print(df)
    return df

# results_storage()

def store_sql():
    import sqlite3

    df1 = profiling_data() # The statistical values of the data are saved
    df2 = results_storage() # All model's scors are saved
    #df3 = grid_search()

    conn = sqlite3.connect('wine.db')

    df1.to_sql('Data_profiling', conn, if_exists='append', index=False)
    df2.to_sql('Result_storage', conn, if_exists='append', index=False)
    #df3.to_sql('Grid_search', conn, if_exists='append', index=False)

    conn.close()

    print("All data is saved in SQLite")

# store_sql()


def main():
    
    store_sql()  # All saved data is stored in sqlite



if __name__ == "__main__":
    main()




