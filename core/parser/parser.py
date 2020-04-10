import math
import csv

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
        data_frame.to_csv('anime_san.csv', quoting=csv.QUOTE_ALL)
        data = {
            "genres": _get_genres(data_frame),
            "ratings": _get_ratings(data_frame)
        }
    else:
        data = {
            "default": data_frame
        }
    return data

def _transform_ratings(rating):
    if rating <= 4:
        return "low"
    elif rating <= 6:
        return "med"
    elif rating <= 8:
        return "high"
    else:
        return "max"

def _get_ratings(data_frame):
    return data_frame['rating'].value_counts().sort_index()

def _get_genres(data_frame):
    genres = data_frame['genre'].value_counts().sort_index()
    _others = genres.tail(len(genres) - 10)
    _others = _others.sum()
    genres = genres.head(10)
    genres = genres.append(pd.Series(_others, index=['Others']))
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
    data_frame = data_frame.reindex()

    data_frame['genre'] = data_frame['genre'].apply(lambda x: x.split(", "))
    data_frame = data_frame.explode('genre')

    data_frame['rating'] = data_frame['rating'].apply(lambda x: math.ceil(x))
    data_frame['rating'] = data_frame['rating'].apply(_transform_ratings)
    data_frame = data_frame.drop(data_frame[data_frame['episodes'] == 'Unknown'].index)

    return data_frame.sort_index()
    