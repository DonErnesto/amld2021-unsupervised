"""
Data preparation for KDD cup data.
The result of this script is input for the workshop participants.

This dataset has 3 categorical variables, and seems to give good results with outlier algorithms

Done here:
- transformation from byte-type strings to regular utf8 strings
- mapping of outliers: 'yes'/'no' to 1/0
- shuffling of data

Necessary preparation during the workshop:
- Removal of duplicates
(NB: df.duplicated(df.drop(columns=['id']).columns).sum() shows there are duplicates)
- (For some algorithms) normalization, categorical encoding

"""

import numpy as np
import pandas as pd
from scipy.io import arff

# Path definitions
X_PATH = "data/x_kdd.pkl"
Y_PATH_1 = "private/y_kdd.pkl"
Y_PATH_2 = r"/Users/ernstoldenhof/Projects/AMLD2020_workshop/API/unsupervised-label-api-pg/data/y_kdd.pkl"


kddcup_path = r"bigdata/KDDCup99_original.arff"


# Load data
data = arff.loadarff(kddcup_path)

df = pd.DataFrame(data[0])

# Convert byte columns to regular strings
str_df_columns = df.select_dtypes([np.object]).columns
for col in str_df_columns:
    df[col] = df[col].str.decode("utf-8")
    df[col] = df[col].apply(lambda x: x.lstrip("'").rstrip("'"))
df.outlier = df.outlier.map({"yes": 1, "no": 0})

# Shuffle the columns
df = df.sample(frac=1, random_state=2718)
df = df.drop(columns="id")
df = df.drop_duplicates()
df = df.reset_index(drop=True)


print("len df: {}".format(len(df)))
assert len(df) == 48113
# Pickle the output
df.drop(columns="outlier").to_pickle(X_PATH)
df.outlier.to_pickle(Y_PATH_1)
df.outlier.to_pickle(Y_PATH_2)

print("Written output to: {}".format(X_PATH))
print("Written output to: {}".format(Y_PATH_1))
print("Written output to: {}".format(Y_PATH_2))
