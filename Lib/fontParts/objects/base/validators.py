# -*- coding: utf8 -*-

from base import FontPartsError

# -------
# Generic
# -------

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

# Color

def validateColor(value):
    if not isinstance(value, (tuple, list)):
        raise FontPartsError("Colors must be tuple instances, not %s." % type(value).__name__)
    if not len(value) == 4:
        raise FontPartsError("Colors must contain four values, not %d." % len(value))
    for component, v in zip("rgba", value):
        if v < 0 or v > 1:
            raise FontPartsError("The value for the %s component (%s) is not between 0 and 1." % (component, v))
    return tuple(value)

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

# -------
# Anchors
# -------

def validateAnchorName(value):
    if not isinstance(value, basestring):
        raise FontPartsError("Anchor names must be unicode strings, not %s." % type(value).__name__)
    return unicode(value)
