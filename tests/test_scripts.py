# coding: utf-8

import os
import subprocess

import unittest

from pymatgen.ext.matproj import MPRester

module_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          '..', 'matminer_examples')

citrine_key = os.environ.get("CITRINE_KEY")
mpds_key = os.environ.get("MPDS_KEY")
mp_key = MPRester().api_key


class ScriptExampleTest(unittest.TestCase):
    def test_kernel_ridge_SCM_OFM(self):
        path = os.path.join(module_dir,
                            "machine_learning-py",
                            "kernel_ridge_SCM_OFM.py")
        # Run in debug mode
        _script_run(path, extra_args=['--debug'])

    def test_figrecipes(self):
        fr_dir = os.path.join(module_dir, 'figrecipes-py')
        # List of scripts to test, note that we don't test 'extras'
        # because of online functionality and 'heatmap' needs to be resolved
        tests = ['bar', 'histogram', 'parallel_coordinates',
                 'scatter_matrix', 'violin', 'xy']
        for test in tests:
            output = _script_run(os.path.join(fr_dir, '{}.py'.format(test)))


def _script_run(path, extra_args=None):
    """
    Execute a script and collect output.

    Args:
        path (str): file path for script
        extra_args (list): additional args for running script

    Returns: script output

    """
    dirname, __ = os.path.split(path)
    os.chdir(dirname)
    args = ["python", path]
    if extra_args:
        args.extend(extra_args)
    output = subprocess.check_call(args)
    return output


if __name__ == "__main__":
    unittest.main()
