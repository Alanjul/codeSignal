#load dataset
import seaborn as sns
import matplotlib.pyplot as pyt

import pandas as pd
import numpy as np
"""sibsp (number of siblings/spouse  aboard
parch (number of parents/children aboard"""
titanic_df = sns.load_dataset('titanic')
#create new _feature family size
titanic_df['family_size'] = titanic_df['sibsp'] + titanic_df['parch'] +1
print(titanic_df.head())
#define the bin edges
age_bins = [0,12,18, 30, 45, 100]
#define bin labels
age_labels = ['child', 'Teenager', 'Young Adult', 'Middle Age', 'Senior']
#create the age group feature with cut to categorize the numerical values into discrete bins
titanic_df['age_group'] = pd.cut(titanic_df['age'], bins=age_bins, labels=age_labels)
print(titanic_df.head(10))
print(titanic_df.age_group.value_counts())

#divide fare by age to create a new feature  fare_per_age . using dataframe operations Any non_number should be replaced with zero
titanic_df['age'] = pd.to_numeric(titanic_df.age, errors='coerce').fillna(0)
titanic_df['fare'] = pd.to_numeric(titanic_df.fare, errors='coerce').fillna(0)
titanic_df['fare_per_age'] = titanic_df.apply(lambda row : row['fare']/row['age'] if row['age'] != 0 else 0, axis=1)
print("fare_per_age column is added")
print(titanic_df.head())