import numpy as np
import pandas as pd
from scipy.stats import f_oneway
from scipy.stats import ttest_ind


# t Student
# standar error = se
se_width = iris.std()['sepal-width']/np.sqrt(10)
se_length = iris.std() ['sepal-length']/np.sqrt(10)

# standar error deviation

sed = np.sqrt (se_length**2)+(se_width**2)
t_stat=(iris.mean()['sepal-length'] - iris.mean()['sepal-width'])/sed

p= ttest_ind (iris ["sepal-length"], iris ["sepal-width"])
# t_test