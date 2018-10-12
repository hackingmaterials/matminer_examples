# coding: utf-8

import os
import subprocess
import tempfile

import nbformat
import unittest

from matminer.data_retrieval.retrieve_MP import MPDataRetrieval

module_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          '..', 'notebooks')

citrine_key = os.environ.get("CITRINE_KEY")
mpds_key = os.environ.get("MPDS_KEY")
mp_key = MPDataRetrieval().mprester.api_key


class NotebookExampleTest(unittest.TestCase):
    def test_intro_predicting_bulk_modulus(self):
        path = os.path.join(module_dir, "intro_predicting_bulk_modulus.ipynb")
        _notebook_run(path)

    @unittest.skipIf(citrine_key is None, "CITRINE_KEY env variable not set.")
    def test_experiment_vs_computed_bandgap(self):
        path = os.path.join(module_dir, "experiment_vs_computed_bandgap.ipynb")
        _notebook_run(path)

    @unittest.skipIf(not all([citrine_key, mpds_key, mp_key]),
                     "data retrieval keys not set")
    def test_get_data(self):
        path = os.path.join(module_dir, "data_retrieval_basics.ipynb")
        _notebook_run(path)

    @unittest.skipIf(mpds_key is None, "MPDS_KEY env variable not set")
    def test_uo_bondlengths(self):
        path = os.path.join(module_dir, "u-o_bondlength_analysis.ipynb")
        _notebook_run(path)

    def test_visualization_with_figrecipes(self):
        path = os.path.join(module_dir, "visualization_with_figrecipes.ipynb")
        _notebook_run(path)

    @unittest.skipIf(not all([mp_key, citrine_key]))
    def test_advanced_visualization(self):
        path = os.path.join(module_dir, "advanced_visualization.ipynb")
        _notebook_run(path)


def _notebook_run(path):
    """
    Execute a notebook via nbconvert and collect output.

    Taken from
    https://blog.thedataincubator.com/2016/06/testing-jupyter-notebooks/

    Args:
        path (str): file path for the notebook object

    Returns: (parsed nb object, execution errors)

    """
    dirname, __ = os.path.split(path)
    os.chdir(dirname)
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=60",
                "--output", fout.name, path]
        subprocess.check_call(args)

        fout.seek(0)
        nb = nbformat.read(fout, nbformat.current_nbformat)

    errors = [output for cell in nb.cells if "outputs" in cell
              for output in cell["outputs"]\
              if output.output_type == "error"]

    return nb, errors


if __name__ == "__main__":
    unittest.main()
