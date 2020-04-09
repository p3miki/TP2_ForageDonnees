import math
import pandas

def parse_data(data_frame, job):
    """Used to filter the data before returning the data frame
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    data_frame.dropna(inplace=True)

    if job == 1:
        data_frame = data_frame.loc[data_frame['Year'] != 2020]
        data_frame = data_frame.loc[data_frame['Year'] != 2017]

        return {
            "global": _global_sales(data_frame),
            "console": _console_sales(data_frame),
            "region": _region_sales(data_frame)
        }
    elif job == 2:
        return {
            "sanitized_data": _sanitize(data_frame)
        }
    else:
        return {
            "default": data_frame
        }

def _global_sales(data_frame):
    return data_frame.groupby(['Genre'])['Global_Sales'].sum().sort_values()


def _console_sales(data_frame):
    return data_frame.groupby(['Platform'])['Global_Sales'].sum().sort_values()


def _region_sales(data_frame):
    return data_frame.groupby(['Year']) \
        .agg({'NA_Sales': 'sum', 'EU_Sales': 'sum', 'JP_Sales': 'sum', 'Other_Sales': 'sum'})

def _sanitize(data_frame):
    del data_frame['name']

    data_frame['rating'] = data_frame['rating'].apply(lambda x: math.ceil(x))
    return data_frame.sort_index()
    