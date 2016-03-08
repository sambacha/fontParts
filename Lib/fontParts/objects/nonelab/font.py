import os
import defcon
from fontParts.objects.base import BaseFont, FontPartsError

class RFont(BaseFont):

    # ---------------
    # File Operations
    # ---------------

    # Initialize

    def _init(self, pathOrObject=None, showInterface=True, **kwargs):
        if isinstance(pathOrObject, basestring):
            font = defcon.Font(pathOrObject)
        elif pathOrObject is None:
            font = defcon.Font()
        else:
            font = pathOrObject
        self._wrapped = font

    # path

    def _get_path(self):
        return self._wrapped.path

    # save

    def _save(self, path=None, showProgress=False, formatVersion=None, **kwargs):
        self._wrapped.save(path=path, formatVersion=formatVersion)

    # close

    def _close(self, *args, **kwargs):
        del self._wrapped
