import pandas
import math

def parse_data(data_frame):
    """Used to filter the data before returning the data frame
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    data_frame.dropna(inplace=True)

    return {
        "sanitized_data": _sanitize(data_frame)
    }


def _sanitize(data_frame):
    del data_frame['name']

    data_frame['rating'] = data_frame['rating'].apply(lambda x: math.ceil(x))
    return data_frame.sort_index()