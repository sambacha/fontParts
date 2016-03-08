# fontParts

This may be the new version of RoboFab. Maybe.

## Why?

RoboFab was written incrementally when we (Erik, Just, Tal) were switching to FontLab. We, and a lot of other designers, had a bunch of important scripts from RoboFog that were crucial to our workflows. The FontLab API was very different from the RoboFog API. It also crashed if the scripter didn't follow some very specific, very unusual practices. We wrote some helper functions to make FontLab a bit more stable during script execution. Those functions grew into a set of object wrappers on top of the FontLab Python objects. These wrappers had a very similar API to the RoboFog API. Once it was in place, we could often run old scripts in FontLab with only a few import changes. (Portable APIs are awesome!!!) This worked so well that we made a version of RoboFab that could operate outside of FontLab. Then we merged them. Then we made a [file format](http://unifiedfontobject.org). Then...we kind of stopped working on RoboFab because it did 253% of what we needed it to. Unfortunately, this incremental, dam-hole-plugging approach to developing RoboFab resulted in some brittle and awkwardly structured code. Still, it worked for > 10 years.

UFO 3 introduced some new object types, object attributes and data types. Tal tried to expand the old RoboFab to cover it, but the old code was not flexible enough. It was very difficult to subclass which made environment specific implementations more difficult than it should have been. It had a huge number of FontLab specific hacks imbedded in places that they shouldn't be. It had so much cruft that it was hard to navigate. Making it work with UFO 3 was not feasible.

We're going to have to start over. Script portability is crucial for type designers. It's also beneficial to the developers of font editors as they won't have to spend time developing a friendly scripting API and it will lower the resistance to change among potential customers.

## Why not call this RoboFab?

This will not be 100% backwards compatible with Robofab. It's going to be as backwards compatible with the "important parts" of RoboFab. So, calling it *RoboFab* would lead to a lot of confusion. We're calling this *fontParts* because that's what it is. It's a collection of objects that represent the parts of fonts.

## Development Plan

This is the plan for development. As tasks are assigned, they will be noted here. ~~Strike through~~ indicates that the step has been completed.

### Compile and refine the current RoboFab API.

- ~~Gustavo: compile the existing object reference into a set of reference documents.~~
- Tal: sketch the new API in a set of base objects with documentation strings.
- *Volunteer?:* Help answer the questions tagged with XXX in the sketch.
- *Volunteer?:* Produce a reference of the objects, methods, arguments and keyword arguments of the existing RoboFab. This could probably done with something like PyDoc. We'll need this to check the new API against to see what has changed.
- Everyone: Review the new API in comparison with the existing API. Discuss and come to some resolution about what should go and what should stay.

#### Things still to do in the API sketch.

- `font.selection` and the various `selected` attributes.
- Classes for subobjects need to be defined in the parent objects. For example, `font.newGlyph` needs to know which class to use for wrapping the newly created glyph.
- Should BaseFont be a subclass of BaseLayer? Font has the same API as BaseLayer plus a few other things.
- Should BaseFont and BaseLayer have `copy` methods? If every object has a copy method, this wouldn't be hard to implement.
- Layers need a visibility API.
- The various `removeXXX` methods have inconsistent arguments. Some take index, some take names and other take objects. Try to unify this so that:
-- when an objects have unique names, use the name.
-- when objects are ordered, use the object or the index.
-- allow as many of these as possible in each method, but have a preference.
- The various transformation methods should all have `center` arguments like `scale` does.
- The `skew` transformation needs to accept (x, y), not just x.
- Should the glyph object have access to the layer order? If glyphs could have a different order than the font a small public lib key will need to be added to the UFO spec.
- Likewise, should glyphs be able to have a color that is different from the font layer color?
- Need to document the various argument value possibilities. For example, if None can be used that needs to be documented.
- `BaseComponent` and `BaseImage` both have a `scale` method and a `scale` attribute. That won't work.
- We need to make clear that two wrapper objects that wrap the same environment object must return True for `__cmp__` and `__eq__`. This will be needed for the obj.index attributes.
- Should the font.save method have a format argument? Guessing the format during a save as operation is tricky. Or, maybe generate is the method that should be used for saving to a different format (sort of like Illustrator's "Save a copy...".

#### Subclassing.

We need to make subclassing very easy.

- The base classes will handle validation of incoming data so that the subclasses will know what they are getting.
- The documentation will be very clear about what subclasses need to implement. It should also say that everything else should be left alone.
- Ideally there would be a subclassing template that contains only the objects and methods that the subclasses must and may want to override. Ideally ideally this could be automatically generated from the base objects so that we don't have to manually maintain two lists.

This is how attributes will be handled:

```python
    type = dynamicProperty("base_type", "The point type. The options are move, line, curve, qcurve, offcurve.")

    def _get_base_type(self):
      return self._get_type()

    def _set_base_type(self, value):
      if value not in ("move", "line", "curve", "qurve", "offcurve"):
        raise FontPartsError("Unknown point type: %r" % value)
      self._set_type(value)

    def _get_type(self):
        """
        Subclasses must implement this.
        """
        self.raiseNotImplementedError()

    def _set_type(self, value):
        """
        Subclasses must implement this.
        """
        self.raiseNotImplementedError()
```

Methods that the scripter calls directly will be handled similarly.

### Build a test suite.

This is necessary to ensure the consistent behavior from environment to environment.

*Volunteers needed.*

### Build a base implementation.

This will be a high-level implementation of the library that implements as many object methods as possible. The goal is to provide as many things "for free" to the subclasses. Anything that can be implemented entirely with the object API should be included. Anything that requires environment specific interaction must by handled by subclasses. This will be done in the API documentation developed in the first step.

- Tal: build the first draft.

#### Dependencies

We need to be very careful about dependencies outside of the standard library. These are the required external dependencies:

- fontTools: needed for lots of stuff.
- fontMath: needed for the font math operations. (requires fontTools, ufoLib [for PointPen])

### Build a reference implementation.

This will be the replacement for NoneLab. It will be built on top of defcon.

*Volunteers needed.*

### Other stuff.

- We need to look through the various modules in RoboFab and see if there are any that we should retain. For example, the classic gString.
- We need to consider how to handle the naming of environment specific methods. An environment may have a `font.blahBlahBlah(foo, bar)` method. In 10 years, we may want to implement our own version of `font.blahBlahBlah()` and we may not want the same API as the environment's API.