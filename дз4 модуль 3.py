import pandas as pd
data = pd.Series([1, 2, 3, 4], index=['a','b','a','c'])
print(data)
ptint(data['a'])


dict_data = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5}
limited_keys = ['a', 'c', 'e']

limited_series = pd.Series(dict_data, index=limited_keys)
print(limited_series)

squares_series = pd.Series([i**2 for i in range(1,21)])
print(squares_series)

filtered_series = squares_series[squares_series.index % 3 != 0]


stundents_df = pd.read_cvs("stundents.csv")
ptint(stundents_df.head(3))
ptint(stundents_df.tail(1))
stundents_df.info()