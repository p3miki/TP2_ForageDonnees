import pandas as pd


def load_file():
    """Returns a dataframe containing the data from the csv file (data.csv)
    :returns:pd.DataFrame"""
    try:
        return pd.read_csv("./core/loader/anime.csv", index_col="anime_id")
    except FileNotFoundError as err:
        print(err)
