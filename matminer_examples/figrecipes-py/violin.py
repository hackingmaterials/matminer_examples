"""
PlotlyFig examples of bar plots.
"""

from matminer import PlotlyFig
from matminer.datasets import load_dataset

__author__ = "Alex Dunn <ardunn@lbl.gov>"


def simple_violin():
    df = load_dataset("elastic_tensor_2015")
    pf = PlotlyFig(df, title="Distribution of Elastic Constant Averages",
                   colorscale='Reds')
    pf.violin(cols=['K_Reuss', 'K_Voigt', 'G_Reuss', 'G_Voigt'],
              use_colorscale=True)


if __name__ == "__main__":
    simple_violin()
