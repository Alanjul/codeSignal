import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler #for data scaling
from sklearn.preprocessing import MinMaxScaler, RobustScaler

#Load the dataset and drop rows with missing values
titanic_df = sns.load_dataset('titanic').dropna()

#initializer the standardScaler
#standardScaler: Normally distributed  and scales it to have zero mean and unit variance
std_scaler = StandardScaler()

#Fit and transform the 'age' column
titanic_df['age'] = std_scaler.fit_transform(np.array(titanic_df['age']).reshape(-1,1))

#check the transformed age column
print(titanic_df['age'].head())

#initialize the MinMaxScaler
min_max_scaler = MinMaxScaler()

#check for the tranformed 'fare' column
print(titanic_df['fare'].head())

#initialize the RobustScaler
robust_scaler = RobustScaler()

#Fit and Transform the 'fare' column
titanic_df['fare'] = robust_scaler.fit_transform(np.array(titanic_df['fare']).reshape(-1,1))
#check the transforemd fare column
print(titanic_df['fare'].head())

