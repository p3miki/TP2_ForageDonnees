import pandas


def parse_data(data_frame):
    """Used to filter the data before returning the data frame
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    data_frame.dropna(inplace=True)
    data_frame = data_frame.loc[data_frame['Year'] != 2020]
    data_frame = data_frame.loc[data_frame['Year'] != 2017]

    return {
        "global": _global_sales(data_frame),
        "console": _console_sales(data_frame),
        "region": _region_sales(data_frame)
    }


def _global_sales(data_frame):
    return data_frame.groupby(['Genre'])['Global_Sales'].sum().sort_values()


def _console_sales(data_frame):
    return data_frame.groupby(['Platform'])['Global_Sales'].sum().sort_values()


def _region_sales(data_frame):
    return data_frame.groupby(['Year']) \
        .agg({'NA_Sales': 'sum', 'EU_Sales': 'sum', 'JP_Sales': 'sum', 'Other_Sales': 'sum'})
