# coding: utf-8

import os
import subprocess
import tempfile

import unittest

module_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          '..', 'scripts')

citrine_key = os.environ.get("CITRINE_KEY")
mpds_key = os.environ.get("MPDS_KEY")
mp_key = MPRester().api_key

class ScriptExampleTest(unittest.TestCase):
    @unittest.skipIf(mp_key is None, "MP API key not set in .pmgrc.yaml")
    def test_kernel_ridge_SCM_OFM(self):
        path = os.path.join(module_dir, "kernel_ridge_SCM_OFM.py")
        _script_run(path)

    def test_figrecipes(self):
        fr_dir = os.path.join(module_dir, '..', 'figrecipes')
        # List of scripts to test, note that we don't test 'extras'
        # because of online functionality and 'heatmap' needs to be resolved
        #TODO: resolve heatmap discrepancy with main repo
        tests = ['bar', 'histogram', 'parallel_coordinates',
                'scatter_matrix', 'violin', 'xy']
        for test in tests:
            output = _script_run(os.path.join(fr_dir, '{}.py'.format(test)))

def _script_run(path):
    """
    Execute a script and collect output.

    Args:
        path (str): file path for script

    Returns: script output

    """
    dirname, __ = os.path.split(path)
    os.chdir(dirname)
    args = ["python", path]
    output = subprocess.check_call(args)
    return output


if __name__ == "__main__":
    unittest.main()