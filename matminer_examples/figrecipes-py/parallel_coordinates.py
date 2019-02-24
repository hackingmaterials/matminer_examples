"""
PlotlyFig examples of parallel coordinates plots.
"""

from matminer.datasets import load_dataset
from matminer import PlotlyFig

__author__ = "Alex Dunn <ardunn@lbl.gov>"


def basic_parallel_coordinates():
    df = load_dataset("elastic_tensor_2015")
    pf = PlotlyFig(df, title="Elastic tensor dataset", colorscale='Jet')
    pf.parallel_coordinates(colors='volume')


if __name__ == "__main__":
    basic_parallel_coordinates()