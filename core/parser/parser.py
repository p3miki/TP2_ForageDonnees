import math
from collections import Counter
from itertools import chain
import pandas as pd

def parse_data(data_frame, job):
    """Used to filter the data before returning the data frame
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    data_frame.dropna(inplace=True)
    data = {}

    if job == 1:
        data_frame = data_frame.loc[data_frame['Year'] != 2020]
        data_frame = data_frame.loc[data_frame['Year'] != 2017]

        data = {
            "global": _global_sales(data_frame),
            "console": _console_sales(data_frame),
            "region": _region_sales(data_frame)
        }
    elif job == 2:
        data_frame = _sanitize(data_frame)
        data = {
            "genres": _get_genres(data_frame),
            "ratings": _get_ratings(data_frame)
        }
    else:
        data = {
            "default": data_frame
        }
    return data

def _get_ratings(data_frame):
    ratings = data_frame['rating'].value_counts().sort_index()

    return ratings


def _get_genres(data_frame):
    genres = pd.Series(Counter(chain(*data_frame.genre)))
    genres = genres.sort_index().rename_axis('genre').reset_index(name='count')
    genres = genres.sort_values(by='count', ascending=False)

    _others = genres.tail(len(genres) - 10)
    genres = genres.head(10)
    genres = genres.append({'genre': 'Others', 'count': _others.sum()['count']}, ignore_index=True)
    return genres

def _global_sales(data_frame):
    return data_frame.groupby(['Genre'])['Global_Sales'].sum().sort_values()


def _console_sales(data_frame):
    return data_frame.groupby(['Platform'])['Global_Sales'].sum().sort_values()


def _region_sales(data_frame):
    return data_frame.groupby(['Year']) \
        .agg({'NA_Sales': 'sum', 'EU_Sales': 'sum', 'JP_Sales': 'sum', 'Other_Sales': 'sum'})

def _sanitize(data_frame):
    del data_frame['name']

    data_frame['genre'] = data_frame['genre'].apply(lambda x: x.split(", "))
    _index_to_drop = []

    for index, row in data_frame.iterrows():
        for genre in row.genre:
            if genre == 'Hentai':
                _index_to_drop.append(index)

    for index in _index_to_drop:
        data_frame = data_frame.drop(index)

    data_frame['rating'] = data_frame['rating'].apply(lambda x: math.ceil(x))
    data_frame.to_csv('test.csv')

    return data_frame.sort_index()
    