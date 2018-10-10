"""
PlotlyFig examples of heatmap plots.
"""

import numpy as np
import pandas as pd
from matminer import PlotlyFig
from matminer.datasets import load_dataset
from matminer.featurizers.structure import GlobalSymmetryFeatures, \
    DensityFeatures

__author__ = "Alireza Faghaninia  <alireza.faghaninia@gmail.com>"


def plot_simple_heatmap_df():
    """
    Very basic example shows how heatmap_df takes a dataframe and returns
    an overview heatmap of the data with the help of pandas.qcut

    Returns:
        plotly plot in "offline" mode poped in the default browser.
    """
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [2, 4, 6, 8, 10, 2, 4, 6, 8, 10]
    c = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    df = pd.DataFrame(data=np.asarray([a, b, c]).T,
                      columns=['var a', 'var b', 'var c'])
    pf = PlotlyFig(colorscale='Oregon')
    pf.heatmap_df(df, x_labels=['low','high'], y_labels=['q1','q2','q3','q4'])


def plot_basic_heatmap():
    """
    Very basic heatmap plot when the data is already in the right format.
    Duplicate example; see https://plot.ly/python/heatmaps/ for more info

    Returns:
        plotly plot in "offline" mode poped in the default browser.
    """
    pf = PlotlyFig(filename='heatmap_basic')
    z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]]
    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    y=['Morning', 'Afternoon', 'Evening']
    pf.heatmap_basic(z, x_labels=x, y_labels=y)


def plot_mean_elastic_tensors():
    """
    An example of heatmap_df where the input data is real and in dataframe
    format. We want to look at how average of the elastic constant tensor
    changes with the density and crystal system. Note that density is not
    a categorical variable in the final dataframe.

    Returns:
        plotly plot in "offline" mode poped in the default browser.
    """
    df = load_dataset("elastic_tensor_2015")
    # data preparation:
    df['Mean Elastic Constant'] = df['elastic_tensor'].apply(lambda x: np.mean(x))
    gs = GlobalSymmetryFeatures(desired_features=['crystal_system'])
    df = gs.featurize_dataframe(df, col_id='structure')
    dsf = DensityFeatures(desired_features=['density'])
    df = dsf.featurize_dataframe(df, col_id='structure')
    # actual plotting
    pf = PlotlyFig(fontscale=0.75, filename='static_elastic_constants', colorscale='RdBu')
    pf.heatmap_df(df[['crystal_system', 'density', 'Mean Elastic Constant']])


if __name__ == '__main__':
    plot_simple_heatmap_df()
    plot_basic_heatmap()
    plot_mean_elastic_tensors()