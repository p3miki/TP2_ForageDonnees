import pandas as pd


def load_file(path, job):
    """Returns a dataframe containing the data from the csv file (data.csv)
        :returns:pd.DataFrame"""
    try:
        return pd.read_csv(path, index_col="anime_id" if job == 2 else "Rank")
    except FileNotFoundError as err:
        print(err)
