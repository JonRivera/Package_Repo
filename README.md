# Package_Repo
Unit 3 Package Repositories

## Main Features
* Contains a module which includes a function that is able to 
output null values of columns in data frame into "pretty format".
* Able to create features with low cardinality

* Examples of applying function outputting null values in pretty format
```python
>>>from package0 import data_null_check
>>> df1 = pd.DataFrame({'a': [NaN, 3, 4, 5], 'b': [1, NaN, 5, 7]})
>>> data_null_check(df1)
a    1
b    1

```

* Example2
```python
>>> df2 = pd.DataFrame({'b': [NaN, 7, 8, 9, 10]})
>>> data_null_check(df2)
>>> data_null_check(df2)
b    1
dtype: int64

```

* Example of low cardinality feature selection
```python
>>> df = pd.read_csv("https://raw.githubusercontent.com/JonRivera/JonRivera.github.io/master/Unit2/Buil_Week/Data_Sets/Hotel_Bookings/hotel_bookings.csv")

>>> df.head()
          hotel  is_canceled  lead_time  arrival_date_year  ... required_car_parking_spaces  total_of_special_requests  reservation_status  reservation_status_date
0  Resort Hotel            0        342               2015  ...                           0                          0           Check-Out               2015-07-01
1  Resort Hotel            0        737               2015  ...                           0                          0           Check-Out               2015-07-01
2  Resort Hotel            0          7               2015  ...                           0                          0           Check-Out               2015-07-02
3  Resort Hotel            0         13               2015  ...                           0                          0           Check-Out               2015-07-02
4  Resort Hotel            0         14               2015  ...                           0                          1           Check-Out               2015-07-03

[5 rows x 32 columns]

>>> features_select(df,'reservation_status')
(['is_canceled', 'lead_time', 'arrival_date_year', 'arrival_date_week_number', 'arrival_date_day_of_month', 'stays_in_weekend_nights', 'stays_in_week_nights', 'adults', 'children', 'babies', 'is_repeated_guest', 'previous_cancellations', 'previous_bookings_not_canceled', 'booking_changes', 'agent', 'company', 'days_in_waiting_list', 'adr', 'required_car_parking_spaces', 'total_of_special_requests', 'hotel', 'arrival_date_month', 'meal', 'market_segment', 'distribution_channel', 'reserved_room_type', 'assigned_room_type', 'deposit_type', 'customer_type'], 'reservation_status')

 ```
# Where to get it
https://github.com/JonRivera/Package_Repo/blob/master/README.md

# Dependencies
* Numpy
* Pandas

# How to install it
pip install -i https://test.pypi.org/simple/ lambdata-JonRivera



