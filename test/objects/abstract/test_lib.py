from fontParts.objects.abstract.lib import Lib


class TestLib(object):

    def test_initializes(arg):
        lib = Lib()
        lib.foo = "bar"
        assert lib.foo is "bar"
