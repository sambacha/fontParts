# -*- coding: utf8 -*-

from base import FontPartsError

"""
XXX

Each of these functions should document what they test for.

XXX
"""

# ----
# Font
# ----

def validatorFileFormatVersion(value):
    if not isinstance(value, (int, float)):
        raise FontPartsError("File format versions must be instances of int or float, not %s." % type(value).__name__)
    return value

def validateLayerOrder(value, font):
    """
    XXX

    - all must exist
    - no duplicates

    XXX
    """
    return value

def validateDefaultLayer(value, font):
    if value not in font.layerOrder:
        raise FontPartsError("No layer with the name %r exists." % value)
    return unicode(value)

# -----
# Layer
# -----

def validateLayerName(value):
    if not isinstance(value, basestring):
        raise FontPartsError("Layer names must be strings, not %s." % type(value).__name__)
    if len(value) < 1:
        raise FontPartsError("Layer names must be at least one character long.")
    return unicode(value)

# -----
# Glyph
# -----

def validateGlyphName(value):
    """
    XXX implement
    """
    return value

def validateGlyphUnicodes(value):
    """
    XXX implement
    """
    return value

def validateGlyphUnicode(value):
    """
    XXX implement
    """
    return value

def validateGlyphWidth(value):
    """
    XXX implement
    """
    return value

def validateGlyphLeftMargin(value):
    """
    XXX implement
    """
    return value

def validateGlyphRightMargin(value):
    """
    XXX implement
    """
    return value

def validateGlyphHeight(value):
    """
    XXX implement
    """
    return value

def validateGlyphBottomMargin(value):
    """
    XXX implement
    """
    return value

def validateGlyphTopMargin(value):
    """
    XXX implement
    """
    return value

# -------
# Contour
# -------

def validateContourIndex(value):
    """
    XXX implement
    """
    return value

def validateContour(value):
    """
    XXX implement
    """
    return value

# -----
# Point
# -----

def validatePointType(value):
    """
    XXX implement
    """
    return value

def validatePointName(value):
    """
    XXX implement
    """
    return value

# -------
# Segment
# -------

def validateSegmentType(value):
    """
    XXX implement
    """
    return value

# ---------
# Component
# ---------

def validateComponentIndex(value):
    """
    XXX implement
    """
    return value

def validateComponent(value):
    """
    XXX implement
    """
    return value

# ------
# Anchor
# ------

def validateAnchorIndex(value):
    """
    XXX implement
    """
    return value

def validateAnchor(value):
    """
    XXX implement
    """
    return value

def validateAnchorName(value):
    if not isinstance(value, basestring):
        raise FontPartsError("Anchor names must be unicode strings, not %s." % type(value).__name__)
    return unicode(value)

# ---------
# Guideline
# ---------

def validateGuidelineIndex(value):
    """
    XXX implement
    """
    return value

def validateGuideline(value):
    """
    XXX implement
    """
    return value

def validateGuidelineAngle(value):
    """
    XXX implement
    """
    return value

def validateGuidelineName(value):
    """
    XXX implement
    """
    return value

# -------
# Generic
# -------

def validateBoolean(value):
    if isinstance(value, int):
        value = bool(value)
    if not isinstance(value, bool):
        raise FontPartsError("Boolean values must be True or False, not %r." % value)
    return value

# Identification

def validateIndex(value):
    if value is not None:
        if not isinstance(value, int):
            raise FontPartsError("Indexes must be None or integers, not %s." % type(value).__name__)
    return value

def validateIdentifier(value):
    if not isinstance(value, basestring):
        raise FontPartsError("Identifiers must be strings, not %s." % type(value).__name__)
    if len(value) > 100:
        raise FontPartsError("The identifier string has a langth (%d) greater than the maximum allowed (100)." % len(value))
    for c in value:
        v = ord(c)
        if v < 0x20 or v > 0x7E:
            raise FontPartsError("The identifier string (%r) contains a character out size of the range 0x20 - 0x7E." % value)
    return value

# Coordinates

def validateX(value):
    if not isinstance(value, (int, float)):
        raise FontPartsError("X coordinates must be instances of int or float, not %s." % type(value).__name__)
    return value

def validateY(value):
    if not isinstance(value, (int, float)):
        raise FontPartsError("Y coordinates must be instances of int or float, not %s." % type(value).__name__)
    return value

def validateCoordinateTuple(value):
    if not isinstance(value, (tuple, list)):
        raise FontPartsError("Coordinates must be tuple instances, not %s." % type(value).__name__)
    if len(value) != 2:
        raise FontPartsError("Coordinates must be tuples containing two items, not %d." % len(value))
    x, y = value
    x = validateX(x)
    y = validateY(y)
    return (x, y)

def validateBoundingBox(value):
    """
    XXX implement
    """
    return value

# Color

def validateColor(value):
    from color import Color
    if not isinstance(value, (tuple, list, Color)):
        raise FontPartsError("Colors must be tuple instances, not %s." % type(value).__name__)
    if not len(value) == 4:
        raise FontPartsError("Colors must contain four values, not %d." % len(value))
    for component, v in zip("rgba", value):
        if v < 0 or v > 1:
            raise FontPartsError("The value for the %s component (%s) is not between 0 and 1." % (component, v))
    return tuple(value)

# File Path

def validateFilePath(value):
    if not isinstance(value, basestring):
        raise FontPartsError("File paths must be strings, not %s." % type(value).__name__)
    return value

# ---------------
# Transformations
# ---------------

def validateTransformationMatrix(value):
    if not isinstance(value, (tuple, list)):
        raise FontPartsError("Transformation matrices must be tuple instances, not %s." % type(value).__name__)
    if not len(value) == 6:
        raise FontPartsError("Transformation matrices must contain six values, not %d." % len(value))
    for v in value:
        if not isinstance(v, (int, float)):
            raise FontPartsError("Transformation matrix values must be instances of int or float, not %s." % type(value).__name__)
    return tuple([float(v) for v in value])

def validateTransformationOffset(value):
    return validateCoordinateTuple(value)

def validateTransformationAngle(value):
    if not isinstance(value, (int, float)):
        raise FontPartsError("Angles must be instances of int ot float, not %s." % type(value).__name__)
    if value < 0 or value > 360:
        raise FontPartsError("The value for the angle (%s) is not between 0 and 1." % value)
    return float(value)

def validateTransformationScale(value):
    """
    XXX implement
    """
    if isinstance(value, (int, float)):
        value = (value, value)
    return value


