"""
PlotlyFig examples of histogram plots.
"""

from matminer.datasets import load_dataset
from figrecipes import PlotlyFig

__author__ = "Alex Dunn <ardunn@lbl.gov>"


def basic_histogram():
    """
    Here we plot a basic histogram showing the distribution of band gaps
    in the matminer dielectric constant dataset, originally taken from Petousis
    et al., 2017.
    """
    df = load_dataset("dielectric_constant")
    pf = PlotlyFig(title="Distribution of Band Gaps in the Dielectric Constant "
                         "Dataset",
                   x_title="Band Gap (eV)",
                   hoverinfo='y')
    pf.histogram(df['band_gap'])


if __name__ == "__main__":
    basic_histogram()
