import unittest

class TestImports(unittest.TestCase):

    def test_imports_work(self):
        """Should raise ImportError if natnetclient doesn't import."""
        import natnetclient

