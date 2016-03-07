from base import FontPartsError

# Strings

def validateString(value):
    if not isinstance(value, basestring):
        raise FontPartsError("Coordinates must be tuple instances, not %s." % type(value).__name__)
    return unicode(value)

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
