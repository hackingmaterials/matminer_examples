"""
PlotlyFig examples of scatter matrix plots.
"""

from matminer.datasets import load_dataset
from matminer import PlotlyFig

__author__ = "Alireza Faghaninia  <alireza.faghaninia@gmail.com>"


def plot_scatter_matrix():
    """
    A few different scatter matrix plots using elastic dataset in matminer.
    Returns:
        plotly plot in "offline" mode opened in the default browser.
    """
    df = load_dataset("elastic_tensor_2015")
    pf = PlotlyFig(df)

    # basic matrix:
    pf.scatter_matrix(cols=['K_VRH', 'G_VRH', 'nsites', 'volume'])

    # with colorscale and labels:
    pf.scatter_matrix(cols=['K_VRH', 'G_VRH', 'nsites', 'volume'],
                      colors='nsites',
                      labels='material_id',
                      colorscale='Picnic')

    # with all the numerical columns included (note the change in sizes):
    pf = PlotlyFig(filename='scatter_matrix_elastic', fontscale=0.6)
    pf.scatter_matrix(df, marker_scale=0.6)


if __name__ == '__main__':
    plot_scatter_matrix()
