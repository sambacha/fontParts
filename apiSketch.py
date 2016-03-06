# ----
# Font
# ----

# File Operations

"path/to/file" = font.path
font.open("path/to/file", showInterface=True)
font.save("optional/path/to/file", showProgress=True, formatVersion=3)
font.close(save=True)
font.generate("otfcff", "optional/path/to/file.otf")

# Sub-Objects

info = font.info
groups = font.groups
kerning = font.kerning
features = font.features
lib = font.lib

# Layers

immutableListOfLayerObjects = font.layers
["layer", "names"] = font.layerOrder
font.layerOrder = ["layer", "names"]
"layer name" = font.defaultLayer
font.defaultLayer = "layer name"
layerObject = font.getLayer("layer name")
layerObject = font.newLayer("layer name", color=(1, 0, 0, 0.5))
layerObject = font.insertLayer(layerObject, name=None, color=None) # XXX this needs to be added to the base code
font.removeLayer(layerObject)

# Glyphs
# - All apply/refer to the font's default layer.

glyphCount = len(font)
for glyphObject in font:
	pass
glyphObject = font["glyph name"]
["glyph", "names"] = font.keys()
bool = "glyph name" in font
glyphObject = font.newGlyph("glyph name")
font.removeGlyph("glyph name")
glyphObject = font.insertGlyph(glyphObject, name="glyph name")
["glyph", "names"] = font.glyphOrder
font.glyphOrder = ["glyph", "names"]

# Operations

font.round()
font.autoUnicodes()

# Guidelines

immutableListOfGuidelineObjects = font.guidelines
guidelineObject = font.appendGuideline(position=(10, 20), angle=75.0, name="optional name", color=None)
font.removeGuideline(guidelineObject)
font.clearGuidelines()

# Interpolation

font.interpolate(0.5, minFont=font1, maxFont=font2, suppressError=True, analyzeOnly=False, showProgress=True)

# Reference Mappings
# - All refer to the font's default layer.

{unicode : ["glyph", "names"]} = font.characterMapping()
{"base glyph": ["glyph", "names"]} = font.getReverseComponentMapping()

# ----
# Info
# ----

# This still needs to be defined.
# It will be very similar, if not
# identical, to RoboFab.

# ------
# Groups
# ------

# This implements all dict operations.

["group", "names"] = groups.findGlyph("glyph name")

# -------
# Kerning
# -------

# This implements all dict operations.

# Math

kerning.add(10)
kerning.scale(2.0)
kerning.round(10)

# Interpolation

kerning.interpolate(0.5, minKerning=kerning1, maxKerning=kerning2, clearExisting=True) # XXX factor is the third arg in the base code. change that.

# --------
# Features
# --------

".fea text" = features.text
features.text = ".fea text"

# ---
# Lib
# ---

# This implements all dict operations.

# -----
# Layer
# -----

# Attributes

"layer name" = layer.name
layer.name = "layer name"
(1, 0, 0, 0.5) = layer.color
layer.color = (1, 0, 0, 0.5)

# Sub-Objects

lib = layer.lib

# Glyphs

10 = len(layer)
for glyphObject in layer:
	pass
glyphObject = layer["glyph name"]
["glyph", "names"] = layer.keys()
bool = "glyph name" in layer
glyphObject = layer.newGlyph("glyph name")
layer.removeGlyph("glyph name")
glyphObject = layer.insertGlyph(glyphObject, name="glyph name")

# Operations

layer.round()
layer.autoUnicodes()

# Interpolation

layer.interpolate(0.5, minLayer=layer1, maxLayer=layer2, suppressError=True, analyzeOnly=False, showProgress=True)

# Reference Mappings

{unicode : ["glyph", "names"]} = layer.characterMapping()
{"base glyph": ["glyph", "names"]} = layer.getReverseComponentMapping()

# -----
# Glyph
# -----

# Name

"glyph name" = glyph.name
glyph.name = "glyph name"

# Unicodes

[unicode, values] = glyph.unicodes
glyph.unicodes = [unicode, values]
unicodeValue = glyph.unicode
glyph.unicode = unicodeValue
glyph.autoUnicodes()

# Metrics

100 = glyph.width
glyph.width = 100
100 = glyph.height
glyph.height = 100
50 = glyph.leftMargin
glyph.leftmargin = 50
50 = glyph.rightMargin
glyph.rightmargin = 50

# Math (glyph math is supported)

# Pens

pen = glyph.getPen()
pointPen = glyph.getPointPen()
glyph.draw(pen)
glyph.drawPoints(pointPen)

# Contours, Components and Anchors

glyph.clear()

2 = len(glyph)
immutableListOfContourObjects = glyph.contours
contourObject = glyph[0]
for contourObject in glyph:
	pass
contourObject = glyph.appendContour(contourObject, offset=(10, 20))
glyph.removeContour(index)
glyph.clearContours()
glyph.removeOverlap()

immutableListOfComponentObjects = glyph.components
componentObject = glyph.components[0]
for componentObject in glyph.components:
	pass
componentObject = glyph.appendComponent("base glyph name", offset=(10, 20), scale=(0.5, 0.5))
glyph.removeComponent(componentObject)
glyph.clearComponents()
glyph.decompose()

immutableListOfAnchorObjects = glyph.anchors
anchorObject = glyph.anchors[0]
for anchorObject in glyph.anchors:
	pass
anchorObject = glyph.appendAnchor("anchor name", position=(10, 20), color=None) # XXX the base code has color listed as mark. it should be color.
glyph.removeAnchor(anchorObject)
glyph.clearAnchors()

glyph.appendGlyph(otherGlyphObject, offset=(10, 20))

# Guidelines

immutableListOfGuidelineObjects = glyph.guidelines
guidelineObject = glyph.appendGuideline(position=(10, 20), angle=75.0, name="optional name", color=None)
glyph.removeGuideline(guidelineObject)
glyph.clearGuidelines()

# Normalization

glyph.round()
glyph.correctDirection()
glyph.autoContourOrder()

# Transformations

glyph.transform((1, 0, 0, 1, 0, 0))
glyph.move((10, 20))
glyph.scale((1.0, 2.0), center=(200, 200))
glyph.rotate(75.0, offset=(10, 20))
glyph.skew(10.0, offset=(10, 20))

# Interpolation

glyph.interpolate(0.5, minGlyph=glyph1, maxGlyph=glyph2, suppressError=True, analyzeOnly=False)
True, ["error", "list"] = glyph.isCompatible(otherGlyphObject, report=True)

# Queries

True = glyph.pointInside((10, 20), evenOdd=False)
(xMin, yMin, xMax, yMax) = glyph.box # also will return a None-like object when the glyph is empty

# Layers

immutableListOfLayerObjects = glyph.layers
layerObject = glyph.getLayer("layer name")
layerObject = glyph.newLayer("layer name")
glyph.removeLayer(layerObject)

# Misc.

(1, 0, 0, 0.5) = glyph.markColor
glyph.markColor = (1, 0, 0, 0.5)
"note" = glyph.note
glyph.note = "note"
libObject = glyph.lib
imageObject = glyph.image
glyph.image = imageObject

# -------
# Contour
# -------

# Identification

1 = contour.index
contour.index = 1
"identifier" = contour.identifier

# Pens

contour.draw(pen)
contour.drawPoints(pointPen)

# Normalization

contour.round()
contour.autoStartSegment()

# Transformations

contour.transform((1, 0, 0, 1, 0, 0))
contour.move((10, 20))
contour.scale((1.0, 2.0), center=(200, 200))
contour.rotate(75.0, offset=(10, 20))
contour.skew(10.0, offset=(10, 20))

# Winding Direction

True = contour.clockwise
contour.clockwise = True
contour.reverseContour() # XXX should this be "reverse"?

# Queries

True = contour.pointInside((10, 20), evenOdd=False)
(xMin, yMin, xMax, yMax) = contour.box # also will return a None-like object when the glyph is empty

# Segments

immutableListOfSegmentObjects = contour.segments
2 = len(contour)
segmentObject = contour[1]
for segmentObject in contour:
	pass
segmentObject = contour.appendSegment("line", [(10, 20)], smooth=False)
segmentObject = contour.insertSegment(2, "line", [(10, 20)], smooth=False)
contour.removeSegment(2)
contour.setStartSegment(2)

# bPoints

immutableListOfBPointObjects = contour.bPoints
2 = len(contour.bPoints)
bPointObject = contour.bPoints[1]
for bPointObject in contour.bPoints:
	pass
bPointObject = contour.appendBPoint("corner", (10, 20))
bPointObject = contour.insertBPoint(2, "corner", (10, 20))

# Points

immutableListOfPointObjects = contour.points
2 = len(contour.points)
pointObject = contour.points[1]
for pointObject in contour.points:
	pass

# -------
# Segment
# -------

# ------
# bPoint
# ------

# -----
# Point
# -----

# ---------
# Component
# ---------

# ------
# Anchor
# ------

# -----
# Image
# -----

# ---------
# Guideline
# ---------