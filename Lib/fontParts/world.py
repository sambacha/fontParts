def OpenFont(path, showInterface=True):
    """
    Open font located at **path**. If **showInterface**
    is ``False``, the font should be opened without
    graphical interface. The default for **showInterface**
    is ``True``.

    ::

        from fontParts.world import *

        font = OpenFont("/path/to/my/font.ufo")
        font = OpenFont("/path/to/my/font.ufo", showInterface=False)
    """
    return dispatcher["OpenFont"](path=path, showInterface=showInterface)

def NewFont(familyName=None, styleName=None, showInterface=True):
    """
    Create a new font. **familyName** will be assigned
    to ``font.info.familyName`` and **styleName**
    will be assigned to ``font.info.styleName``. These
    are optional and default to ``None``. If **showInterface**
    is ``False``, the font should be created without
    graphical interface. The default for **showInterface**
    is ``True``.

    ::

        from fontParts.world import *

        font = NewFont()
        font = NewFont(familyName="My Family", styleName="My Style")
        font = NewFont(showInterface=False)
    """
    return dispatcher["NewFont"](familyName=familyName, styleName=styleName, showInterface=showInterface)

def CurrentFont():
    """
    Get the "current" font.
    """
    return dispatcher["CurrentFont"]()

def CurrentGlyph():
    """
    Get the "current" glyph from :func:`CurrentFont`.

    ::

        from fontParts.world import *

        glyph = CurrentGlyph()
    """
    return dispatcher["CurrentGlyph"]()

def CurrentLayer():
    """
    Get the "current" layer from :func:`CurrentGlyph`.

    ::

        from fontParts.world import *

        layer = CurrentLayer()
    """
    return dispatcher["CurrentLayer"]()

def CurrentContours():
    """
    Get the "currently" selected contours from :func:`CurrentGlyph`.

    ::

        from fontParts.world import *

        contours = CurrentContours()
    """
    return dispatcher["CurrentContours"]()

def CurrentSegments():
    """
    Get the "currently" selected segments from :func:`CurrentContours`.

    ::

        from fontParts.world import *

        segments = CurrentSegments()
    """
    return dispatcher["CurrentSegments"]()

def CurrentPoints():
    """
    Get the "currently" selected points from :func:`CurrentContours`.

    ::

        from fontParts.world import *

        points = CurrentPoints()
    """
    return dispatcher["CurrentPoints"]()

def CurrentComponents():
    """
    Get the "currently" selected components from :func:`CurrentGlyph`.

    ::

        from fontParts.world import *

        components = CurrentComponents()
    """
    return dispatcher["CurrentComponents"]()

def CurrentAnchors():
    """
    Get the "currently" selected anchors from :func:`CurrentGlyph`.

    ::

        from fontParts.world import *

        anchors = CurrentAnchors()
    """
    return dispatcher["CurrentAnchors"]()

def CurrentGuidelines():
    """
    Get the "currently" selected guidelines from :func:`CurrentGlyph`.
    This may include both font level and glyph level guidelines.

    ::

        from fontParts.world import *

        guidelines = CurrentGuidelines()
    """
    return dispatcher["CurrentGuidelines"]()


def AllFonts():
    """
    Get a list of all open fonts.

    * XXX should this include fonts with showInterface=False?
    * XXX define the special sorting methods that must be in the return object.

    ::

        from fontParts.world import *

        fonts = AllFonts()
        for font in fonts:
            # do something
    """
    return dispatcher["AllFonts"]()

def RFont(path=None, showInterface=True):
    return dispatcher["RFont"](path=path, showInterface=showInterface)

def RGlyph():
    return dispatcher["RGlyph"]()

# ----------
# Dispatcher
# ----------

class _EnvironmentDispatcher(object):

    def __init__(self, registryItems):
        self._registry = {item: None for item in registryItems}

    def __setitem__(self, name, func):
        self._registry[name] = func

    def __getitem__(self, name):
        func = self._registry[name]
        if func is None:
            raise NotImplementedError
        return func

dispatcher = _EnvironmentDispatcher([
    "OpenFont",
    "NewFont",
    "AllFonts",
    "CurrentFont",
    "CurrentGlyph",
    "CurrentLayer",
    "CurrentContours",
    "CurrentSegments",
    "CurrentPoints",
    "CurrentComponents",
    "CurrentAnchors",
    "CurrentGuidelines",
    "RFont",
    "RGlyph"
])

# -------
# NoneLab
# -------

try:
    from fontParts import nonelab

    # OpenFont, RFont

    def _NoneLabRFont(path=None, showInterface=True):
        return nonelab.RFont(pathOrObject=path, showInterface=showInterface)

    dispatcher["OpenFont"] = _NoneLabRFont
    dispatcher["RFont"] = _NoneLabRFont

    # NewFont

    def _NoneLabNewFont(familyName=None, styleName=None, showInterface=True):
        font = nonelab.RFont(showInterface=showInterface)
        if familyName is not None:
            font.info.familyName = familyName
        if styleName is not None:
            font.info.styleName = styleName
        return font

    dispatcher["NewFont"] = _NoneLabNewFont

except ImportError:
    pass
