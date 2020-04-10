import sys
from collections import Counter
from itertools import chain

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def update_view(data_frames, job):
    """Plots the graphs with the data provided"""
    if job == 2:
        # print(data_frame)
        plot_genres(data_frames['genres'])
        plot_rating(data_frames['ratings'])
    else:
        afficher_regions(data_frames['region'])
        afficher_globales(data_frames['global'])
        afficher_consoles(data_frames['console'])

def plot_genres(data_frame):
    """Prints total count of genres of anime
        :param data_frame
        :type data_frame: pandas.DataFrame"""
    data_frame.plot(kind='pie', y='count')
    plt.title('Nombre d\'anime par genres')
    _show(plt)

def plot_rating(data_frame):
    """Print total count for each rating
        :param data_frame
        :type data_frame: pandas.DataFrame"""
    data_frame.plot(kind='bar')
    plt.title('Nombre d\'anime par classification')
    _show(plt)

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
