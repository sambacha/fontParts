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
    return dispatcher["NewFont"](familyName=familyName, styleName=styleName,
                                 showInterface=showInterface)


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

    This returns an immutable list, even when nothing is selected.
    """
    return dispatcher["CurrentContours"]()


def _defaultCurrentContours():
    glyph = CurrentGlyph()
    if glyph is None:
        return ()
    return glyph.selectedContours


def CurrentSegments():
    """
    Get the "currently" selected segments from :func:`CurrentContours`.

    ::

        from fontParts.world import *

        segments = CurrentSegments()

    This returns an immutable list, even when nothing is selected.
    """
    return dispatcher["CurrentSegments"]()


def _defaultCurrentSegments():
    glyph = CurrentGlyph()
    if glyph is None:
        return ()
    segments = []
    for contour in glyph.selectedContours:
        segments.extend(contour.selectedSegments)
    return tuple(segments)


def CurrentPoints():
    """
    Get the "currently" selected points from :func:`CurrentContours`.

    ::

        from fontParts.world import *

        points = CurrentPoints()

    This returns an immutable list, even when nothing is selected.
    """
    return dispatcher["CurrentPoints"]()


def _defaultCurrentPoints():
    glyph = CurrentGlyph()
    if glyph is None:
        return ()
    points = []
    for contour in glyph.selectedContours:
        points.extend(contour.selectedPoints)
    return tuple(points)


def CurrentComponents():
    """
    Get the "currently" selected components from :func:`CurrentGlyph`.

    ::

        from fontParts.world import *

        components = CurrentComponents()

    This returns an immutable list, even when nothing is selected.
    """
    return dispatcher["CurrentComponents"]()


def _defaultCurrentComponents():
    glyph = CurrentGlyph()
    if glyph is None:
        return ()
    return glyph.selectedComponents


def CurrentAnchors():
    """
    Get the "currently" selected anchors from :func:`CurrentGlyph`.

    ::

        from fontParts.world import *

        anchors = CurrentAnchors()

    This returns an immutable list, even when nothing is selected.
    """
    return dispatcher["CurrentAnchors"]()


def _defaultCurrentAnchors():
    glyph = CurrentGlyph()
    if glyph is None:
        return ()
    return glyph.selectedAnchors


def CurrentGuidelines():
    """
    Get the "currently" selected guidelines from :func:`CurrentGlyph`.
    This will include both font level and glyph level guidelines.

    ::

        from fontParts.world import *

        guidelines = CurrentGuidelines()

    This returns an immutable list, even when nothing is selected.
    """
    return dispatcher["CurrentGuidelines"]()


def _defaultCurrentGuidelines():
    guidelines = []
    font = CurrentFont()
    if font is not None:
        guidelines.extend(font.selectedGuidelines)
    glyph = CurrentGlyph()
    if glyph is not None:
        guidelines.extend(glyph.selectedGuidelines)
    return tuple(guidelines)


def AllFonts(sortBy=None):
    """
    Get a list of all open fonts. Optionally, provide a
    value for ``sortBy`` to sort the fonts. See
    :func:`world.SortFonts` for options.

    ::

        from fontParts.world import *

        fonts = AllFonts()
        for font in fonts:
            # do something

        fonts = AllFonts(sortBy="magic")
        for font in fonts:
            # do something
    """
    fonts = dispatcher["AllFonts"]()
    if sortBy is not None:
        font = SortFonts(fonts)
    return fonts


def RFont(path=None, showInterface=True):
    return dispatcher["RFont"](path=path, showInterface=showInterface)


def RGlyph():
    return dispatcher["RGlyph"]()

# ------------
# Font Sorting
# ------------

def SortFonts(fonts, sortBy="magic"):
    """
    Sort ``fonts`` with the ordering preferences defined
    by ``sortBy``. ``sortBy`` must be one of the following:

    * sort description string
    * sort value function
    * list/tuple containing strings and/or sort value functions
    * ``"magic"``

    The sort description strings, and how they sort, are:

    +--------------------+--------------------------------------+
    | ``"familyName"``   | Family names by alphabetical order.  |
    +--------------------+--------------------------------------+
    | ``"styleName"``    | Style names by alphabetical order.   |
    +--------------------+--------------------------------------+
    | ``"isItalic"``     | Italics before romans.               |
    +--------------------+--------------------------------------+
    | ``"isRoman"``      | Romans before italics.               |
    +--------------------+--------------------------------------+
    | ``"widthValue"``   | Width values by numerical order.     |
    +--------------------+--------------------------------------+
    | ``"weightValue"``  | Weight values by numerical order.    |
    +--------------------+--------------------------------------+
    | ``"monospace"``    | Monospaced before proportional.      |
    +--------------------+--------------------------------------+
    | ``"proportional"`` | Proportional before monospaced.      |
    +--------------------+--------------------------------------+

    A sort value function must be a function that accepts
    one argument, ``font``. This function must return
    a sortable value for the given font. For example:

    ::

        def glyphCountSortValue(font):
            return len(font)

    A list of sort description strings and/or sort functions
    may also be provided. This should be in order of most
    to least important. For example, to sort by family name
    and then style name, do this:

    ::

        fonts = SortFonts(fonts, ["familyName", "styleName"])

    If "magic" is given for ``sortBy``, the fonts will be
    sorted based on this sort description sequence:

    * ``"familyName"``
    * ``"isProportional"``
    * ``"widthValue"``
    * ``"weightValue"``
    * ``"styleName"``
    * ``"isRoman"``

    """
    from types import FunctionType
    from fontTools.misc.py23 import basestring
    valueGetters = dict(
        familyName=_sortValue_familyName,
        styleName=_sortValue_styleName,
        isRoman=_sortValue_isRoman,
        isItalic=_sortValue_isItalic,
        widthValue=_sortValue_widthValue,
        weightValue=_sortValue_weightValue,
        isProportional=_sortValue_isProportional,
        isMonospace=_sortValue_isMonospace
    )
    if not isinstance(sortBy, (tuple, list)):
        if sortBy == "magic":
            sortBy = [
                "familyName",
                "isProportional",
                "widthValue",
                "weightValue",
                "styleName",
                "isRoman"
            ]
        elif isinstance(sortBy, basestring) or isinstance(sortBy, FunctionType):
            sortBy = (sortBy,)
        else:
            raise ValueError("Unknown sortBy value: %s" % repr(sortBy))
    if not len(sortBy) >= 1:
        raise ValueError(
            "sortBy must contain at least one sort description string or function."
        )
    sorter = []
    for font in fonts:
        sortable = []
        for valueName in sortBy:
            valueGetter = valueGetters.get(valueName, valueName)
            if not isinstance(valueGetter, FunctionType):
                raise ValueError("Unknown sortBy value type: %s" % str(type(valueGetter)))
            value = valueGetter(font)
            sortable.append(value)
        sortable.append(font)
        sortable = tuple(sortable)
    sorter.sort()
    return [i[-1] for i in sorter]

def _sortValue_familyName(font):
    """
    Returns font.info.familyName.
    """
    return font.info.familyName

def _sortValue_styleName(font):
    """
    Returns font.info.styleName.
    """
    return font.info.styleName

def _sortValue_roman(font):
    """
    Returns 0 if the font is roman.
    Returns 1 if the font is not roman.
    """
    italic = _sortValue_italic(font)
    if italic == 1:
        return 0
    return 1

def _sortValue_italic(font):
    """
    Returns 0 if the font is italic.
    Returns 1 if the font is not italic.
    """
    info = font.info
    if info.italicAngle not in (None, 0):
        return 0
    if "italic" in info.styleMapStyleName:
        return 0
    return 1

def _sortValue_widthValue(font):
    """
    Returns font.info.openTypeOS2WidthClass.
    """
    return font.info.openTypeOS2WidthClass

def _sortValue_weightValue(font):
    """
    Returns font.info.openTypeOS2WeightClass.
    """
    return font.info.openTypeOS2WeightClass

def _sortValue_proportional(font):
    """
    Returns 0 if the font is proportional.
    Returns 1 if the font is not proportional.
    """
    monospace = _sortValue_monospace(font)
    if monospace == 1:
        return 0
    return 1

def _sortValue_monospace(font):
    """
    Returns 0 if the font is monospace.
    Returns 1 if the font is not monospace.
    """
    if postscriptIsFixedPitch:
        return 0
    testWidth = None
    for glyph in font:
        if testWidth is None:
            testWidth = glyph.width
        else:
            if testWidth != glyph.width:
                return 1
    return 0


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

# Register the default functions.

dispatcher["CurrentContours"] = _defaultCurrentContours
dispatcher["CurrentSegments"] = _defaultCurrentSegments
dispatcher["CurrentPoints"] = _defaultCurrentPoints
dispatcher["CurrentComponents"] = _defaultCurrentComponents
dispatcher["CurrentAnchors"] = _defaultCurrentAnchors
dispatcher["CurrentGuidelines"] = _defaultCurrentGuidelines

# -------
# fontshell
# -------

try:
    from fontParts import fontshell

    # OpenFont, RFont

    def _fontshellRFont(path=None, showInterface=True):
        return fontshell.RFont(pathOrObject=path, showInterface=showInterface)

    dispatcher["OpenFont"] = _fontshellRFont
    dispatcher["RFont"] = _fontshellRFont

    # NewFont

    def _fontshellNewFont(familyName=None, styleName=None, showInterface=True):
        font = fontshell.RFont(showInterface=showInterface)
        if familyName is not None:
            font.info.familyName = familyName
        if styleName is not None:
            font.info.styleName = styleName
        return font

    dispatcher["NewFont"] = _fontshellNewFont

except ImportError:
    pass
