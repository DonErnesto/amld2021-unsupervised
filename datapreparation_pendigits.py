"""
Data preparation for Pendigits data.
The result of this script is input for the workshop participants.

This dataset has only numerical data (16 columns), with little meaning (originating from
downsampling coordinates in time from digits written on a digital pad)

Done here:
- mapping of outliers: b'yes'/b'no' to 1/0
- shuffling of data

Necessary preparation during the workshop:
- Nothing
"""

import pandas as pd
from scipy.io import arff

# path definitions
X_PATH = "data/x_pendigits.csv"
Y_PATH = "data/y_pendigits.csv"
pendigits_path = "data/PenDigits_withoutdupl_norm_v01.arff"


# load data
data = arff.loadarff(pendigits_path)
df = pd.DataFrame(data[0])
df = df.drop(columns=["id"])
df.outlier = df.outlier.map({b"yes": 1, b"no": 0})
df = df.sample(frac=1, random_state=2718)
df = df.reset_index(drop=True)


# save the output
df.drop(columns="outlier").to_csv(X_PATH, index=False)
print(f"Written features to: {X_PATH}")

df.outlier.to_csv(Y_PATH, index=False)
print(f"Written label to: {Y_PATH}")
