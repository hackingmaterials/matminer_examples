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