"Package0 - a collection of Data Science helpfer functions"

import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split

def data_null_check(df):
  """Prints out nulls of dataframe into a nice data frame format"""
  if type(df)==pd.core.frame.DataFrame:
    return df.isnull().sum()

def features_select(df,name_target,max_cardinality =20):
    """creates features, and target from data frame, takes dataframe, 
    name of feature in strings, and has an optional 3rd parameter of max
    cardinality allowed"""
    target = name_target
    #creating subsets of features, splitted between numerical and categorical
    train_features =  df.drop(columns = [name_target],axis =1)
    numeric_features = train_features.select_dtypes(include='number').columns.tolist()
    cardinality = train_features.select_dtypes(exclude ='number').nunique()
    categorical_features = cardinality[cardinality <= max_cardinality].index.tolist()
    #combine lists to extrapolate features of interest
    features = numeric_features + categorical_features
    return (features, target)


