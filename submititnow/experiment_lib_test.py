# %%
import argparse
from submititnow.experiment_lib import _extract_common_params
import unittest


class TestExtractCommonParams(unittest.TestCase):
    def test_empty_list(self):
        params = []
        result = _extract_common_params(params)
        self.assertEqual(result, {})

    def test_single_param(self):
        params = [argparse.Namespace(a=1, b=2, c=3)]
        result = _extract_common_params(params)
        self.assertEqual(result, {"a": 1, "b": 2, "c": 3})

    def test_multiple_params(self):
        params = [
            argparse.Namespace(a=1, b=2, c=3),
            argparse.Namespace(a=1, b=2, c=4),
            argparse.Namespace(a=1, b=2, c=3, d=5),
        ]
        result = _extract_common_params(params)
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_no_common_params(self):
        params = [
            argparse.Namespace(a=1, b=2),
            argparse.Namespace(c=3, d=4),
            argparse.Namespace(e=5, f=6),
        ]
        result = _extract_common_params(params)
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
