# -*- coding: utf8 -*-

from errors import FontPartsError

"""
XXX

Each of these functions should document what they test for.

XXX
"""

# ----
# Font
# ----

def validatorFileFormatVersion(value):
    """Validates a font's file format version
    
    - value must be a int or float.
    - Returned value is the same as input value.
    """
    
    if not isinstance(value, (int, float)):
        raise FontPartsError("File format versions must be instances of int or float, not %s." % type(value).__name__)
    return value

def validateLayerOrder(value, font):
    """Validates layer order
    
    - value must contain layers that exist in the font.
    - value must not contain duplicate layers.
    - Returned list will be unicode strings for each layer name.
    """
    
    # Test for layer exisiting
    for layer in value:
        if layer not in font.layerOrder:
            raise FontPartsError("No layer with the name %r exists." % value)
    
    # Test for dupes
    import collections.Counter
    duplicates = [item for item, count in Counter(value).items() if count > 1]
    if len(duplicates) != 0:
        raise FontPartsError("Duplicate layers are not allowed. Layer name(s) %r are duplicate." % " ".join(duplicates))
    
    return [unicode(layer) for layer in value]

def validateDefaultLayer(value, font):
    """Validates default layer
    
    - value must be a layer in the font.
    - Returned value will be a unicode string.
    """
    
    if value not in font.layerOrder:
        raise FontPartsError("No layer with the name %r exists." % value)
    return unicode(value)

def validateGlyphOrder(value):
    """
    XXX implement
    """
    return value

# -------
# Kerning
# -------

def validateKerningKey(value):
    """
    XXX implement
    """
    return value

def validateKerningValue(value):
    """
    XXX implement
    """
    return value

# ------
# Groups
# ------

def validateGroupKey(value):
    """
    XXX implement
    """
    return value

def validateGroupValue(value):
    """
    XXX implement
    """
    return value

# --------
# Features
# --------

def validateFeatureText(value):
    """
    XXX implement
    """
    return value

# ---
# Lib
# ---

def validateLibKey(value):
    """
    XXX implement
    """
    return value

def validateLibValue(value):
    """
    XXX implement
    """
    return value

# -----
# Layer
# -----

def validateLayerName(value):
    """Validates layer name
    
    - value must be a string.
    - value must be at least one character.
    - Returned value will be a unicode string.
    """
    
    if not isinstance(value, basestring):
        raise FontPartsError("Layer names must be strings, not %s." % type(value).__name__)
    if len(value) < 1:
        raise FontPartsError("Layer names must be at least one character long.")
    return unicode(value)

# -----
# Glyph
# -----

def validateGlyphName(value):
    """Validates glyph name
    
    - value must be a string.
    - value must be at least one character.
    - Returned value will be a unicode string.
    """
    
    if not isinstance(value, basestring):
        raise FontPartsError("Glyph names must be strings, not %s." % type(value).__name__)
    if len(value) < 1:
        raise FontPartsError("Glyph names must be at least one character long.")
    return unicode(value)

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
    """Validates glyph width
    
    - value must be a int or float.
    - value cannot be negative.
    - Returned value is a float.
    """
    
    if not isinstance(value, (int, float)):
        raise FontPartsError("Glyph width must be an int or float, not %s." % type(value).__name__)
    if value < 0:
        raise FontPartsError("Glyph width must be be 0 or greater.")
    return float(value)

def validateGlyphLeftMargin(value):
    """Validates glyph left margin
    
    - value must be a int or float.
    - Returned value is a float.
    """
    
    if not isinstance(value, (int, float)):
        raise FontPartsError("Glyph left margin must be an int or float, not %s." % type(value).__name__)
    return float(value)

def validateGlyphRightMargin(value):
    """Validates glyph right margin
    
    - value must be a int or float.
    - Returned value is a float.
    """
    
    if not isinstance(value, (int, float)):
        raise FontPartsError("Glyph right margin must be an int or float, not %s." % type(value).__name__)
    return float(value)

def validateGlyphHeight(value):
    """Validates glyph height
    
    - value must be a int or float.
    - value cannot be negative.
    - Returned value is a float.
    """
    
    if not isinstance(value, (int, float)):
        raise FontPartsError("Glyph height must be an int or float, not %s." % type(value).__name__)
    if value < 0:
        raise FontPartsError("Glyph height must be be 0 or greater.")
    return float(value)

def validateGlyphBottomMargin(value):
    """Validates glyph bottom margin
    
    - value must be a int or float.
    - Returned value is a float.
    """
    
    if not isinstance(value, (int, float)):
        raise FontPartsError("Glyph bottom margin must be an int or float, not %s." % type(value).__name__)
    return float(value)

def validateGlyphTopMargin(value):
    """Validates glyph top margin
    
    - value must be a int or float.
    - Returned value is a float.
    """
    
    if not isinstance(value, (int, float)):
        raise FontPartsError("Glyph top margin must be an int or float, not %s." % type(value).__name__)
    return float(value)

# -------
# Contour
# -------

def validateContourIndex(value):
    """Validates contour index
    
    - value must be an int or None.
    - Returned value is the same as input value.
    """
    
    return validateIndex(value)

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
    """Validates point name
    
    - value must be a string.
    - Returned value will be a unicode string.
    """
    
    if not isinstance(value, basestring):
        raise FontPartsError("Point names must be strings, not %s." % type(value).__name__)
    return unicode(value)

# -------
# Segment
# -------

def validateSegmentType(value):
    """
    XXX implement
    """
    return value

# ----
# Type
# ----

def validateBPointType(value):
    """
    XXX implement
    """
    return value

# ---------
# Component
# ---------

def validateComponentIndex(value):
    """Validates component index
    
    - value must be an int or None.
    - Returned value is the same as input value.
    """
    
    return validateIndex(value)

def validateComponent(value):
    """
    XXX implement
    """
    return value

# ------
# Anchor
# ------

def validateAnchorIndex(value):
    """Validates anchor index
    
    - value must be an int or None.
    - Returned value is the same as input value.
    """
    
    return validateIndex(value)

def validateAnchor(value):
    """
    XXX implement
    """
    return value

def validateAnchorName(value):
    """Validates anchor name
    
    - value must be a string.
    - Returned value will be a unicode string.
    """
    
    if not isinstance(value, basestring):
        raise FontPartsError("Anchor names must be strings, not %s." % type(value).__name__)
    return unicode(value)

# ---------
# Guideline
# ---------

def validateGuidelineIndex(value):
    """Validates guideline index
    
    - value must be an int or None.
    - Returned value is the same as input value.
    """
    
    return validateIndex(value)

def validateGuidelineAngle(value):
    """Validates a guideline's angle
    
    - Value must be a int or float.
    - Value must be between -360 and 360.
    - If the value is negative, it is normalized by adding it to 360
    - Returned value is a float between 0 and 360.
    """
    
    if not isinstance(value, (int, float)):
        raise FontPartsError("Guideline angle must be instances of int or float, not %s." % type(value).__name__)
    if abs(value) > 360:
        raise FontPartsError("Guideline angle must be between -360 and 360.")
    if value < 0:
        value = value + 360
    return float(value)

def validateGuidelineName(value):
    """Validates guideline name
    
    - value must be a string.
    - Returned value will be a unicode string.
    """
    
    if not isinstance(value, basestring):
        raise FontPartsError("Guideline names must be strings, not %s." % type(value).__name__)
    return unicode(value)

# -------
# Generic
# -------

def validateBoolean(value):
    """Validates a boolean
    
    - value must be a int with value of 0 or 1, or a boolean.
    - Returned value will be a boolean.
    """
    
    if isinstance(value, int):
        value = bool(value)
    if not isinstance(value, bool):
        raise FontPartsError("Boolean values must be True or False, not %r." % value)
    return value

# Identification

def validateIndex(value):
    """Validates index
    
    - value must be an int or None.
    - Returned value is the same as input value.
    """
    
    if value is not None:
        if not isinstance(value, int):
            raise FontPartsError("Indexes must be None or integers, not %s." % type(value).__name__)
    return value

def validateIdentifier(value):
    """Validates identifier
    
    - value must be an string.
    - value must not be longer than 100.
    - value must not contain a character between the range of 0x20 - 0x7E.
    - Returned value is a unicode string.
    """
    
    if not isinstance(value, basestring):
        raise FontPartsError("Identifiers must be strings, not %s." % type(value).__name__)
    if len(value) > 100:
        raise FontPartsError("The identifier string has a length (%d) greater than the maximum allowed (100)." % len(value))
    for c in value:
        v = ord(c)
        if v < 0x20 or v > 0x7E:
            raise FontPartsError("The identifier string (%r) contains a character out size of the range 0x20 - 0x7E." % value)
    return unicode(value)

# Coordinates

def validateX(value):
    """Validates x coordinate
    
    - value must be an int or float.
    - Returned value is a float.
    """
    
    if not isinstance(value, (int, float)):
        raise FontPartsError("X coordinates must be instances of int or float, not %s." % type(value).__name__)
    return float(value)

def validateY(value):
    """Validates y coordinate
    
    - value must be an int or float.
    - Returned value is a float.
    """
    
    if not isinstance(value, (int, float)):
        raise FontPartsError("Y coordinates must be instances of int or float, not %s." % type(value).__name__)
    return float(value)

def validateCoordinateTuple(value):
    """Validates coordinate tuple
    
    - value must be an tuple.
    - value must be have two items.
    - value items must be an int or float.
    - Returned value is a tuple of two floats.
    """
    
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
    """Validates color
    
    - value must be an tuple, list, or Color.
    - value must be have four items.
    - value color components must be between 0 and 1.
    - Returned value is a tuple.
    """
    
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
    """Validates file path
    
    - value must be a string.
    - Returned value is the same as input value.
    """
    
    if not isinstance(value, basestring):
        raise FontPartsError("File paths must be strings, not %s." % type(value).__name__)
    return value

# Interpolation

def validateInterpolationFactor(value):
    """
    XXX implement
    """
    if isinstance(value, (int, float)):
        value = (value, value)
    return value

# ---------------
# Transformations
# ---------------

def validateTransformationMatrix(value):
    """Validates transformation matrix
    
    - value must be an tuple or list.
    - value must be have six items.
    - value items must be a int or float.
    - Returned value is a tuple of six floats.
    """
    
    if not isinstance(value, (tuple, list)):
        raise FontPartsError("Transformation matrices must be tuple instances, not %s." % type(value).__name__)
    if not len(value) == 6:
        raise FontPartsError("Transformation matrices must contain six values, not %d." % len(value))
    for v in value:
        if not isinstance(v, (int, float)):
            raise FontPartsError("Transformation matrix values must be instances of int or float, not %s." % type(value).__name__)
    return tuple([float(v) for v in value])

def validateTransformationOffset(value):
    """Validates transformation offset
    
    - value must be an tuple.
    - value must be have two items.
    - value items must be an int or float.
    - Returned value is a tuple of two floats.
    """
    
    return validateCoordinateTuple(value)

def validateTransformationRotationAngle(value):
    """Validates transformation angle
    
    - Value must be a int or float.
    - Value must be between -360 and 360.
    - If the value is negative, it is normalized by adding it to 360
    - Returned value is a float between 0 and 360.
    """
    
    if not isinstance(value, (int, float)):
        raise FontPartsError("Angles must be instances of int or float, not %s." % type(value).__name__)
    if abs(value) > 360:
        raise FontPartsError("The value for the angle (%s) is not between -360 and 360." % value)
    if value < 0:
        value = value + 360
    return float(value)

def validateTransformationSkewAngle(value):
    """
    XXX implement
    """
    if isinstance(value, (int, float)):
        value = (value, value)
    return value

def validateTransformationScale(value):
    """
    XXX implement
    """
    if isinstance(value, (int, float)):
        value = (value, value)
    return value

