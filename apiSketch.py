# ----
# Font
# ----

# File Operations

font = Font("path/to/file", showInterface=True)
"path/to/file" = font.path
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
image = glyph.addImage(path)

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

2 = segment.index
"line" = segment.type
segment.type = "line"
False = segment.smooth
segment.smooth = False

# Points

1 = len(segment)
pointObject = segment[0]
for pointObject in point:
	pass
pointObject = segment.onCurve
[pointObjects] = segment.offCurve
pointObject = segment.insertPoint(0, "offcurve", (10, 20))
segment.removePoint(0)

# Transformations

segment.transform((1, 0, 0, 1, 0, 0))
segment.move((10, 20))
segment.scale((1.0, 2.0), center=(200, 200))
segment.rotate(75.0, offset=(10, 20))
segment.skew(10.0, offset=(10, 20))

# Normalization

segment.round()

# ------
# bPoint
# ------

2 = bPoint.index
"corner" = bPoint.type
bPoint.type = "corner"

# Points

pointObject = bPoint.anchor
pointObject = bPoint.bcpIn
pointObject = bPoint.bcpOut

# Transformations

bPoint.transform((1, 0, 0, 1, 0, 0))
bPoint.move((10, 20))
bPoint.scale((1.0, 2.0), center=(200, 200))
bPoint.rotate(75.0, offset=(10, 20))
bPoint.skew(10.0, offset=(10, 20))

# Normalization

bPoint.round()

# -----
# Point
# -----

2 = point.index
"line" = point.type
point.type = "line"
False = point.smooth
point.smooth = False
10 = point.x
point.x = 10
20 = point.y
point.y = 20
"name" = point.name
point.name = "name"
"identifier" = point.identifier

# Transformations

point.transform((1, 0, 0, 1, 0, 0))
point.move((10, 20))
point.scale((1.0, 2.0), center=(200, 200))
point.rotate(75.0, offset=(10, 20))
point.skew(10.0, offset=(10, 20))

# Normalization

point.round()

# ---------
# Component
# ---------

2 = component.index
"glyph name" = component.baseGlyph
component.baseGlyph = "glyph name"
(1, 0, 0, 1, 10, 20) = component.transformation
component.transformation = (1, 0, 0, 1, 10, 20)
(10, 20) = component.offset
component.offset = (10, 20)
(1.0, 1.0) = component.scale
component.scale = (1.0, 1.0)
"identifier" = component.identifier

# Pens

component.draw(pen)
component.drawPoints(pointPen)

# Transformations

component.transform((1, 0, 0, 1, 0, 0))
component.move((10, 20))
component.scale((1.0, 2.0), center=(200, 200))
component.rotate(75.0, offset=(10, 20))
component.skew(10.0, offset=(10, 20))
component.decompose()

# Normalization

point.round()

# ------
# Anchor
# ------

2 = anchor.index
10 = anchor.x
anchor.x = 10
20 = anchor.y
anchor.y = 20
"name" = anchor.name
anchor.name = "name"
"identifier" = point.identifier
(1, 0, 0, 0.5) = anchor.color
anchor.color = (1, 0, 0, 0.5)

# Transformations

anchor.transform((1, 0, 0, 1, 0, 0))
anchor.move((10, 20))
anchor.scale((1.0, 2.0), center=(200, 200))
anchor.rotate(75.0, offset=(10, 20))
anchor.skew(10.0, offset=(10, 20))

# Normalization

anchor.round()

# -----
# Image
# -----

"image name" = image.name
image.name = "image name"
(1, 0, 0, 1, 10, 20) = image.transformation
image.transformation = (1, 0, 0, 1, 10, 20)
(10, 20) = image.offset
image.offset = (10, 20)
(1.0, 1.0) = image.scale
image.scale = (1.0, 1.0)

# Transformations

image.transform((1, 0, 0, 1, 0, 0))
image.move((10, 20))
image.scale((1.0, 2.0), center=(200, 200))
image.rotate(75.0, offset=(10, 20))
image.skew(10.0, offset=(10, 20))
image.decompose()

# Normalization

image.round()

# ---------
# Guideline
# ---------

2 = guideline.index
10 = guideline.x
anchor.x = 10
20 = anchor.y
guideline.y = 20
75.0 = guideline.angle
guideline.angle = 75.0
"name" = guideline.name
guideline.name = "name"
"identifier" = guideline.identifier
(1, 0, 0, 0.5) = guideline.color
guideline.color = (1, 0, 0, 0.5)

# Transformations

guideline.transform((1, 0, 0, 1, 0, 0))
guideline.move((10, 20))
guideline.scale((1.0, 2.0), center=(200, 200))
guideline.rotate(75.0, offset=(10, 20))
guideline.skew(10.0, offset=(10, 20))

# Normalization

guideline.round()