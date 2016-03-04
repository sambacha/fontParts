"""
The goal is to define a very clean scripting API
that preserves the main functionality of RoboFab.
Say something about the importance of script
portability. Designers have workflows and specific
binary requirements, etc.

Things that should be considered for removal:
- anything that does anything too magical.
- anything that was originally implemented for
  environment specific reasons.
- anything that was designed as a speed optimization.

Things that haven't been defined, but should.
- the selected attribute for glyph and below.
- a common error instead of relying on the environment
  errors. those often differ from environment
  to environment and that's a portability problem.
- what errors should be raised by each method
- an interpolation method for all realistic objects.
  this way font.interpolate can just iterate through
  those.
- classes for subobjects need to be declared in the
  parent objects.
- the class to use for a copy operation needs to
  be defined for each object that has a copy method.

Things that we should consider adding:
- a naming convention for environment specific
  things. for example, it would be bad if two
  environments defined "makeMyFont" but they took
  different arguments and did different things.
- a parent tree system like in defcon. this would
  replace the fragile getParent.

-----------
UFO 3 Stuff
-----------

font
----
layers = font.layers
list = font.glyphOrder (or should this go to info?)
guideline = font.guidelines[index]
guideline = font.appendGuideline
font.removeGuideline(index)
font.clearGuidelines

layers
------
list = layers.layerOrder
layer = layers.defaultLayer
layers.defaultLayer = layer
del layer[name]
layer = layers[name]
layer = layers.newLayer(name)
for name in layers:
int = len(layers)
name in layers (also do has_key for consistency)
list = layers.keys()

layer
-----
glyph = layer.newGlyph(same as font)
glyph = layer.insertGlyph(same as font)
for name in layers:
glyph = layer[name]
del layer[name]
int = len(layer)
name in layer (also do has_key for consistency)
list layer.keys()
layer.name = something
something = layer.name
color = layer.color
layer.color = color
layer.componentMapping (same as font)
layer.characterMapping (same as font)
layer.lib

glyph
-----
int = glyph.height
glyph.height = int
color = glyph.markColor
glyph.markColor = color
guideline = glyph.guidelines[index]
guideline = glyph.appendGuideline
glyph.removeGuideline(index)
glyph.clearGuidelines
glyph.image = image
image = glyph.image

contour
-------
# str = contour.identifier
# contour.identifier = str

point
-----
# str = point.identifier
# point.identifier = str

component
---------
# str = component.identifier
# component.identifier = str

anchor
------
color = anchor.color
anchor.color = color
# str = anchor.identifier
# anchor.identifier = str

image
-----
matrix = image.transformation
image.transformation = matrix
(add scale and offset like in component)
str = image.fileName
image.fileName = str
color = image.color
image.color = color
data = image.data
image.data = data

Don't present an interface to the core image set.
That is very UFO specific. The only tricky thing
that I can think of right now would be if two glyphs
have images with the same name but different data.
That would need to be managed in the defcon wrapper.

guideline
---------
x
y
angle
name
color
identifier

data
----
Don't provide direct access to this. It's very UFO specific.

color
-----
(r, g, b, a)
"""
