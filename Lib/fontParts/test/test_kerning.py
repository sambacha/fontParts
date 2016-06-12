import unittest
from fontParts.base import FontPartsError


class TestKerning(unittest.TestCase):

    def getKerning_generic(self):
        kerning, unreferenced = self.objectGenerator("kerning")
        kerning.update({
            ("public.kern1.X", "public.kern2.X") : 100,
            ("B", "public.kern2.X") : 101,
            ("public.kern1.X", "B") : 102,
            ("A", "A") : 103,
        })
        return kerning, unreferenced

    # ---
    # len
    # ---

    def test_len(self):
        kerning, unreferenced = self.getKerning_generic()
        self.assertEqual(
            len(kerning),
            4
        )
        kerning.clear()
        self.assertEqual(
            len(kerning),
            0
        )