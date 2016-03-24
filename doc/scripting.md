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