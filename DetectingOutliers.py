import numpy as np
import pandas as pd
import seaborn as sns
#load the dataset
titanic_df =sns.load_dataset('titanic')

#remove the rows with missing age data for accurate detection outlier
titanic_df = titanic_df.dropna(subset=['age'])

#calculate the z_score , A z_score of 0 means that the dataset is close to the mean and z_score of 1.0
#indicates a value that is one standard deviation from the mean. High z_score denotes outliers
titanic_df['age_zscore'] = np.abs((titanic_df.age-titanic_df.age.mean())/titanic_df.age.std())

#Getting the rows of outliers using a threshold of 3
outliers_zscore = titanic_df[(titanic_df['age_zscore'] > 3)]
print(outliers_zscore)

#detecting outliers with interquartile ranges
q1 = titanic_df['age'].quantile(0.25)
q3 = titanic_df['age'].quantile(0.75)
IQR = q3- q1

#Define Bounds
lower_bounds = q1 -1.5 * IQR
upper_bounds = q3 + 1.5 * IQR

#Get the rows of outliers according to IQR METHOD
outliers_iqr = titanic_df[(titanic_df['age'] < lower_bounds) | (titanic_df['age'] > upper_bounds)]
print(outliers_iqr)
#using the z_score method
titanic_df = titanic_df[titanic_df['age_zscore'] <= 3]

#using the IQR method to remove outliers
titanic_df = titanic_df[(titanic_df['age'] >= lower_bounds ) & (titanic_df['age'] <= upper_bounds)]

#replacing outliers with mean
titanic_df.loc[titanic_df['age_zscore'] > 3, 'age'] = titanic_df['age'].mean()

#replacing the outliers in age column with the mean
titanic_df.loc[(titanic_df['age'] < lower_bounds) | (titanic_df['age'] > upper_bounds), 'age'] = titanic_df['age'].median()
