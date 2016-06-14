# Implementing fontParts in Your Environment

The base objects have been designed to provide common behavior, validation and type consistency for environments and scripters alike. Environments wrap their native objects with subclasses of fontParts' base objects and implement the necessary translation to the native API. Once this is done, the environment will inherit all of the base behavior from fontParts.

## General Structure

Environments will need to implement their own subclasses of:

- BaseFont
- BaseInfo
- BaseGroups
- BaseKerning
- BaseFeatures
- BaseLib
- BaseGuideline
- BaseLayer
- BaseGlyph
- BaseContour
- BaseSegment
- BaseBPoint
- BasePoint
- BaseComponent
- BaseAnchor
- BaseImage

Each of these require their own specific environment overrides, but the general structure follows this form:

```python
from fontParts.base import BaseSomething

class MySomething(BaseSomething):

	# Initialization.
	# This will be called when objects are initialized.
	# The behavior, args and kwargs may be designed by the
	# subclass to implement specific behaviors.

	def _init(self, myObj):
		self.myObj = myObj

	# Comparison.
	# The __eq__ method must be implemented by subclasses.
	# It must return a boolean indicating if the lower level
	# objects are the same object. This does not mean that two
	# objects that have the same content should be considered
	# equal. It means that the object must be the same.

	def __eq__(self, other):
		return self.myObj == other.myObj

	# Properties.
	# Properties are get and set through standard method names.
	# Within these methods, the subclass may do whatever is
	#	necessary to get/set the value from/to the environment.

	def _get_something(self):
		return self.myObj.getSomething()

	def _set_something(self, value):
		self.myObj.setSomething(value)

	# Methods.
	# Generally, the public methods call internal methods with
	# the same name, but preceded with an underscore. Subclasses
	# may implement the internal method. Any values passed to
	# the internal methods will have been validated and will
	# be a standard type.

	def _whatever(self, value):
		self.myObj.doWhatever(value)

	# Copying.
	# Copying is handled in most cases by the base objects.
	# If subclasses have a special class that should be used
	# when creating a copy of an object, the class must be
	# defined with the copyClass attribute. If anything special
	# needs to be done during the copying process, the subclass
	# can implement the copyData method. This method will be
	# called automatically. The subclass must call the base class
	# method with super.

	copyClass = MyObjectWithoutUI

	def copyData(self, source):
		super(MySomething, self).copyData(source)
		self.myObj.internalThing = source.internalThing

	# Environment updating.
	# If the environment requires the scripter to manually
	# notify the environment that the object has been updated,
	# the subclass must implement the update method. Please
	# try to avoid requiring this.

	def update(self):
		myEnv.goUpdateYourself()

	# Wrapped objects.
	# It is very useful for scripters to have access to the
	# lower level, wrapped object. Subclasses implement this
	# with the naked method.

	def naked(self):
		return self.myObj
```

All methods that must be overridden are labeled with "Subclasses must override this method." in the method's documentation string. If a method may optionally be overridden, the documentation string is labeled with "Subclasses may override this method." All other methods, attributes and properties **must not** be overridden.

An example implementation that wraps the defcon library with fontParts is located in fontParts/objects/nonelab.

## Layers

There are two primary layer models in the font world:

- font level layers: In this model, all glyphs have the same layers. A good example of this is a chromatic font.
- glyph level layers: In this model, individual glyphs may have their own unique layers.

fontParts supports both of these models. Both fonts and glyphs have fully developed layer APIs.

```python
font = CurrentFont()
foregroundLayer = font.getLayer("foreground")
backgroundLayer = font.getLayer("background")

glyph = font["A"]
foregroundGlyph = glyph.getLayer("foreground")
backgroundGlyph = glyph.getLayer("background")
```

A font-level layer is a font-like object. Essentially, a layer has the same glyph management behavior as a font.

```python
font = CurrentFont()
foreground = font.getLayer("foreground")
glyph = foreground.newGlyph("A")
```

A glyph-level layer is identical to a glyph object.

```python
font = CurrentFont()
glyph = font["A"]
foreground = glyph.getLayer("foreground")
background = glyph.getLayer("background")
```

When a scripter is addressing a font or glyph without specifying a specific layer, the action is performed on the "default" (or primary) layer. For example, in the original Fontographer there were two layers: foreground and background. The foreground was the primary layer and it contained the primary data that would be compiled into a font binary. In multi-layered glyph editing environments, designers can specify which layer should be considered primary. This layer is the "default" layer in fontParts. Thus:

```python
font = CurrentFont()
glyph1 = font["A"]
glyph2 = font.newGlyph("B")
```

The `glyph1` object will reference the A's "foreground" layer and the "foreground" layer will contain a new glyph named "B".

fontParts delegates the implementation to the environment subclasses. Given that an environment can only support font-level layers *or* glyph-level layers, the following algorithms can be used to simulate the model that the environment doesn't support.

### Simulating glyph-level layers.

1. Get the parent font.
2. Iterate through all of the font's layers.
3. If the glyph's name is in the layer, grab the glyph from the layer.
4. Return all found glyphs.

### Simulating font-level layers.

1. Iterate over all glyphs.
2. For every layer in the glyph, create a global mapping of layer name to glyphs containing a layer with the same name.
