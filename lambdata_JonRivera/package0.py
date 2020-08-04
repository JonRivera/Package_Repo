"""Package0 - a collection of Data Science helpfer functions"""
import pandas as pd


def data_null_check(df):
    """Prints out nulls of dataframe into a nice data frame format"""
    if type(df) == pd.core.frame.DataFrame:
        return df.isnull().sum()


def features_select(df, name_target, max_cardinality=20):
    """ creates features, and target from data frame, takes dataframe, 
    name of feature in strings, and has an optional 3rd parameter of max
    cardinality allowed"""
    target = name_target
    # creating subsets of features, splitted between numerical and categorical
    train_features = df.drop(columns=[name_target], axis=1)
    numeric_features = train_features.select_dtypes(include='number').columns.tolist()
    cardinality = train_features.select_dtypes(exclude='number').nunique()
    categorical_features = cardinality[cardinality <= max_cardinality].index.tolist()
    # combine lists to extrapolate features of interest
    features = numeric_features + categorical_features
    return features, target


class Car:
    """makes a car class"""

    def __init__(self, mpg=40, horsepower=170, price=25000, color='red'):
        self.mpg = mpg
        self.horsepower = horsepower
        self.price = price
        self.color = color

    def sound(self):
        return "ROOOM"


class Ferrari(Car):
    """ Uses class enheritance to make Ferrari"""

    def __init__(self, mpg, horsepower, price, color, edition='sport'):
        super().__init__(mpg, horsepower, price, color)
        self.edition = edition

    def sound(self):
        return "boom --VROOM"
