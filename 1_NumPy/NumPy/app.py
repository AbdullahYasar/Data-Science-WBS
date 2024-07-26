# your code
import numpy as np
from numpy import random
import pandas as pd


produkt = ["käse", "honig", "schnitzel", "ayran", "kefir", "nudeln"]


def project1(list1, value, top_price):

    titel = random.choice(list1, size=(value, 1))
    id_ = np.arange(1, value+1).reshape(value, 1)
    price = np.round(np.random.uniform(top_price, size=(value, 1)), 2)
    data1 = np.hstack((id_, titel, price))
    return data1


data2 = project1(produkt, 100, 5)


df = pd.DataFrame(data2)
df.columns = ["id", "titel", "price"]


df.to_csv('first_numpy_project.csv', index=False)


