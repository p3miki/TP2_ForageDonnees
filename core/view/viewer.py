import sys

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def update_view(data_frame):
    """Plots the graphs with the data provided"""
    afficher_regions(data_frame['region'])
    afficher_globales(data_frame['global'])
    afficher_consoles(data_frame['console'])


def afficher_globales(data_frame):
    """Prints global sales
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    # dff = data_frame.groupby(['Genre'])['Global_Sales'].sum().sort_values()
    data_frame.plot(kind='bar', rot=1)
    plt.xlabel('Genres de jeu')
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes totales par Genres')
    _maximize(plt.get_current_fig_manager(), plt)
    plt.show()

def afficher_consoles(data_frame):
    """Prints sales by console
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    data_frame.plot(kind='bar', rot=1)
    plt.xlabel('Nom de Console')
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes par Console')
    _maximize(plt.get_current_fig_manager(), plt)
    plt.show()

def afficher_regions(data_frame):
    """Prints sales graph by region
        :param data_frame:
        :type data_frame: pandas.DataFrame"""
    data_frame.plot(rot=1)
    plt.xlabel('Région De Vente')
    plt.ylabel('Ventes (en millions)')
    plt.title('Ventes par région')
    _maximize(plt.get_current_fig_manager(), plt)
    plt.show()


def _maximize(manager, plotter):
    if sys.platform.startswith("linux") and plotter.get_backend() == "TkAgg":
        manager.resize(*manager.window.maxsize())
    elif plotter.get_backend() == "TkAgg":
        manager.window.state('zoomed')
    elif plotter.get_backend() == "wxAgg":
        manager.frame.Maximize(True)
    elif plotter.get_backend() == "Qt4Agg":
        manager.window.showMaximized()
