import weakref
from fontParts.base.errors import FontPartsError
from fontParts.base.base import BaseDict, dynamicProperty
from fontParts.base import normalizers


class BaseGroups(BaseDict):

    """
    An groups object.

        >>> groups = RGroups()
    """

    keyNormalizer = normalizers.normalizeGroupKey
    valueNormalizer = normalizers.normalizeGroupValue

    # -------
    # Parents
    # -------

    def getParent(self):
        """
        Return the groups' parent :class:`fontParts.base.BaseFont`.
        This is a backwards compatibility method.
        """
        return self.font

    # Font

    _font = None

    font = dynamicProperty("font", "The groups' parent :class:`BaseFont`.")

    def _get_font(self):
        if self._font is None:
            return None
        return self._font()

    def _set_font(self, font):
        assert self._font is None or self._font() == font
        if font is not None:
            font = weakref.ref(font)
        self._font = font

    # ---------
    # Searching
    # ---------

    def findGlyph(self, glyphName):
        """
        Return a list of all groups containing glyphName.
        """
        glyphName = normalizers.normalizeGlyphName(glyphName)
        groupNames = self._findGlyph(glyphName)
        groupNames = [self.keyNormalizer(groupName) for groupName in groupNames]
        return groupNames

    def _findGlyph(self, glyphName):
        """
        Subclasses may override this method.
        """
        found = []
        for groupName, groupList in self.items():
            if glyphName in groupList:
                found.append(groupName)
        return found

    # ---------------------
    # RoboFab Compatibility
    # ---------------------

    def remove(self, key):
        """
        This is a backwards compatibility method.
        """
        del self[key]

    def asDict(self):
        """
        This is a backwards compatibility method.
        """
        d = {}
        for k, v in self.items():
            d[k] = v
        return d
