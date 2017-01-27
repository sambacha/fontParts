import unittest
from fontParts.base import FontPartsError


class TestKerning(unittest.TestCase):

    def getKerning_generic(self):
        kerning, unrequested = self.objectGenerator("kerning")
        kerning.update({
            ("public.kern1.X", "public.kern2.X") : 100,
            ("B", "public.kern2.X") : 101,
            ("public.kern1.X", "B") : 102,
            ("A", "A") : 103,
        })
        return kerning, unrequested

    # ---
    # len
    # ---

    def test_len(self):
        kerning, unrequested = self.getKerning_generic()
        self.assertEqual(
            len(kerning),
            4
        )
        kerning.clear()
        self.assertEqual(
            len(kerning),
            0
        )

    # --------
    # contains
    # --------

    def test_contains(self):
        kerning, unrequested = self.getKerning_generic()
        self.assertEqual(
            kerning[('A','A')],
            True
        )
        self.assertEqual(
            kerning[("public.kern1.X", "public.kern2.X")],
            True
        )
        self.assertEqual(
            kerning[("B", "public.kern2.X")],
            True
        )
        self.assertEqual(
            kerning[("H", "H")],
            False
        )

    # ---
    # del
    # ---

    def test_del(self):
        kerning, unrequested = self.getKerning_generic()
        self.assertEqual(
            kerning[('A','A')],
            True
        )
        del kerning[('A','A')]
        self.assertEqual(
            kerning[('A','A')],
            False
        )

    # ---
    # get
    # ---

    def test_get(self):
        kerning, unrequested = self.getKerning_generic()
        self.assertEqual(
            kerning[('A','A')],
            103
        )
        self.assertEqual(
            kerning[("public.kern1.X", "public.kern2.X")],
            100
        )
        self.assertEqual(
            kerning[("B", "public.kern2.X")],
            101
        )
        self.assertEqual(
            kerning[("public.kern2.X", "B")],
            102
        )