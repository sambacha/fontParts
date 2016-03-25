## Font

### Copy

```python
copied = font.copy()
```

Make a copy of the font.

### File Operations

```python
"/path/to/font" = font.path
```


```python
font = Font(pathOrObject=None, showInterface=True)
```

```python
font.save(path=None, showProgress=False, formatVersion=None)
```

I'm starting to think that we should get rid of the formatVersion argument. It allows for a save to convert formats in place. That can get really messy and is probably not what a user wants to do. The generate method is a better way to handle this.


```python
font.close(save=False)
```

I think we should remove the save argument.


```python
font.generate(format, path=None)
```

The format options are:

- mactype1 = Mac Type 1 font (generates suitcase and LWFN file)
- macttf = Mac TrueType font (generates suitcase)
- macttdfont = Mac TrueType font (generates suitcase with resources in data fork)
- otfcff = PS OpenType (CFF-based) font (OTF)
- otfttf = PC TrueType/TT OpenType font (TTF)
- pctype1 = PC Type 1 font (binary/PFB)
- pcmm = PC MultipleMaster font (PFB)
- pctype1ascii = PC Type 1 font (ASCII/PFA)
- pcmmascii = PC MultipleMaster font (ASCII/PFA)
- ufo1 = UFO format version 1
- ufo2 = UFO format version 2
- ufo3 = UFO format version 3
- unixascii = UNIX ASCII font (ASCII/PFA)

Not every environment will support all of these, but we need standard format names.


### Sub-Objects

```python
font.info
```

```python
font.groups
```

```python
font.kerning
```

```python
font.features
```

```python
font.lib
```


### Layers

```python
for layer in font.layers:
	...
```

Immutable list of layers.


```python
layer = font.getLayer("name")
```


```python
layer = font.newLayer("name", color=None)
```


```python
font.removeLayer(name)
```

`name` should be changed to `layer` and accept either a name, an index or a layer object.


```python
["layer", "names"] = font.layerOrder
font.layerOrder = ["layer", "names"]
```


```python
"name" = font.defaultLayer
font.defaultLayer = "name"
```


### Glyphs

```python
for glyph in font:
	...
```


```python
bool = "glyphname" in font
```


```python
glyph = font["glyphname"]
```


```python
numberOfGlyphs = len(font)
```


```python
glyph = font.newGlyph(name)
```


```python
glyph = font.insertGlyph(sourceGlyph, name=None)
```


```python
font.removeGlyph(name)
```

`name` should support a name or a glyph object.


```python
["glyph", "names"] = font.keys()
```


```python
["glyph", "names"] = font.glyphOrder
font.glyphOrder = ["glyph", "names"]
```


### Guidelines

```python
for guideline in font.guidelines:
	...
```

Immutable list of guidelines.


```python
guideline = font.appendGuideline(position, angle, name=None, color=None)
```


```python
font.removeGuideline(guideline)
```

`guideline` can be a guideline object or an index.


```python
font.clearGuidelines()
```

### Interpolation

```python
font.interpolate(factor, minFont, maxFont, round=True, suppressError=True)
```


```python
compatible, report = font.isCompatible(other)
```

Returns a boolean indicating if interpolating between the font and the other font will raise an exception. It also returns a string report describing any compatibility issues.


### Normalization

```python
font.autoUnicodes()
```

Calls `layer.autoUnicodes` on the default layer.


```python
font.round()
```

Calls `round` for all sub-objects that have the method. The default layer is the only layer that will be rounded.


### Environment

```python
font.naked()
```

```python
font.update()
```

## Glyph

### Identification

### Metrics

```python
100 = glyph.width
glyph.width = 100
100 = glyph.leftMargin
glyph.leftMargin = 100
100 = glyph.rightMargin
glyph.rightMargin = 100
```

```python
100 = glyph.height
glyph.height = 100
100 = glyph.bottomMargin
glyph.bottomMargin = 100
100 = glyph.topMargin
glyph.topMargin = 100
```


### Contents

```python
glyph.clear(contours=True, components=True, anchors=True, guidelines=True, image=True)
```

```python
glyph.bounds
```

None or (xMin, yMin, xMax, yMax).


#### Contours



```python
glyph.__getitem__(index)
```

```python
glyph.__iter__()
```

```python
glyph.__len__()
```

```python
glyph.appendContour(contour, offset=None)
```





```python
glyph.appendGlyph(other, offset=None)
```

```python
glyph.clearContours()
```

```python
glyph.removeOverlap()
```


```python
glyph.removeContour(index)
```









#### Components

```python
glyph.appendComponent(baseGlyph, offset=None, scale=None)
```


```python
glyph.clearComponents()
```

```python
glyph.decompose()
```

```python
glyph.removeComponent(component)
```












#### Anchors

```python
glyph.appendAnchor(name, position, color=None)
```

```python
glyph.clearAnchors()
```

```python
glyph.removeAnchor(anchor)
```












#### Guidelines

```python
glyph.appendGuideline(position, angle, name=None, color=None)
```

```python
glyph.clearGuidelines()
```

```python
glyph.removeGuideline(guideline)
```




#### Image

```python
glyph.addImage(path=None, data=None, scale=None, position=None, color=None)
```

```python
glyph.clearImage()
```

### Layers

```python
for glyphLayer in glyph.layers:
	...
```

Immutable list of glyph layers.


```python
glyphLayer = glyph.getLayer("name")
```


```python
glyphLayer = glyph.newLayer("name")
```


```python
glyph.removeLayer(layer)
```

`layer` should accept either a name or a glyph layer object.


### Interpolation and Math

```python
glyph.interpolate(factor, minGlyph, maxGlyph, round=True, suppressError=True)
```


```python
glyph.isCompatible(other)
```

Returns a boolean indicating if interpolating between the glyph and the other glyph will raise an exception. It also returns a string report describing any compatibility issues.


```python
glyph2 = glyph1 * 2.0
glyph2 = glyph1 / 2.0
glyph3 = glyph1 + glyph2
glyph3 = glyph1 - glyph2
```


### Pens and Drawing

```python
glyph.draw(pen, contours=True, components=True)
```


```python
glyph.drawPoints(pen, contours=True, components=True)
```


```python
glyph.getPen()
```


```python
glyph.getPointPen()
```



































```python
glyph.pointInside(point)
```





















```python
glyph.anchors
```



```python
glyph.bottomMargin
```







```python
glyph.components
```



```python
glyph.contours
```



```python
glyph.font
```



```python
glyph.guidelines
```






```python
glyph.image
```



```python
glyph.layer
```



```python
glyph.lib
```



```python
glyph.markColor
```



```python
glyph.name
```



```python
glyph.note
```







```python
glyph.unicode
```



```python
glyph.unicodes
```







```python
glyph.copy()
```



### Transformations


```python
glyph.moveBy(value)
```


```python
glyph.rotateBy(value, origin=None)
```


```python
glyph.scaleBy(value, origin=None)
```


```python
glyph.skewBy(value, origin=None)
```


```python
glyph.transformBy(matrix, origin=None)
```


### Normalization

```python
glyph.round()
```


```python
glyph.autoCorrectDirection(trueType=False)
```


```python
glyph.autoContourOrder()
```


```python
glyph.autoUnicodes()
```


### Environment

```python
font.naked()
```

```python
font.update()
```