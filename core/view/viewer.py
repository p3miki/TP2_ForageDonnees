import sys
from collections import Counter
from itertools import chain

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def update_view(data_frame, job):
    """Plots the graphs with the data provided"""
    if job == 2:
        # print(data_frame)
        _get_genres(data_frame['sanitized_data'])
    else:
        afficher_regions(data_frame['region'])
        afficher_globales(data_frame['global'])
        afficher_consoles(data_frame['console'])

def _get_genres(data_frame):
    genres = pd.Series(Counter(chain(*data_frame.genre)))
    genres = genres.sort_index().rename_axis('genre').reset_index(name='count')
    genres = genres.sort_values(by='count', ascending=False)

    _others = genres.tail(len(genres) - 10)
    genres = genres.head(10)
    genres.reset_index(drop=True, inplace=True)
    genres = genres.append({'genre': 'Others', 'count': _others.sum()['count']}, ignore_index=True)
    print(genres)

def afficher_globales(data_frame):
    """Prints global sales
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    # dff = data_frame.groupby(['Genre'])['Global_Sales'].sum().sort_values()
    data_frame.plot(kind='bar', rot=1)
    plt.xlabel('Genres de jeu')
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes totales par Genres')
    _show(plt)

def afficher_consoles(data_frame):
    """Prints sales by console
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    data_frame.plot(kind='bar', rot=1)
    plt.xlabel('Nom de Console')
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes par Console')
    _show(plt)

def afficher_regions(data_frame):
    """Prints sales graph by region
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    data_frame.plot(rot=1)
    plt.xlabel('Région De Vente')
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes par région')
    _show(plt)

def _show(_plt):
    _maximize(plt.get_current_fig_manager(), _plt)
    _plt.show()

def _maximize(manager, plotter):
    if sys.platform.startswith("linux") and plotter.get_backend() == "TkAgg":
        manager.resize(*manager.window.maxsize())
    elif plotter.get_backend() == "TkAgg":
        manager.window.state('zoomed')
    elif plotter.get_backend() == "wxAgg":
        manager.frame.Maximize(True)
    elif plotter.get_backend() == "Qt4Agg":
        manager.window.showMaximized()
