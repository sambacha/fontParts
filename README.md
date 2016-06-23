# fontParts

This may be the new version of RoboFab. Maybe.

The documentation is being developed concurrrently with the code. You can view the current version at [fontparts.readthedocs.org](http://fontparts.readthedocs.org).

## Why?

RoboFab was written incrementally when we (Erik, Just, Tal) were switching to FontLab. We, and a lot of other designers, had a bunch of important scripts from RoboFog that were crucial to our workflows. The FontLab API was very different from the RoboFog API. It also crashed if the scripter didn't follow some very specific, very unusual practices. We wrote some helper functions to make FontLab a bit more stable during script execution. Those functions grew into a set of object wrappers on top of the FontLab Python objects. These wrappers had a very similar API to the RoboFog API. Once it was in place, we could often run old scripts in FontLab with only a few import changes. (Portable APIs are awesome!!!) This worked so well that we made a version of RoboFab that could operate outside of FontLab. Then we merged them. Then we made a [file format](http://unifiedfontobject.org). Then...we kind of stopped working on RoboFab because it did 253% of what we needed it to. Unfortunately, this incremental, dam-hole-plugging approach to developing RoboFab resulted in some brittle and awkwardly structured code. Still, it worked for > 10 years.

UFO 3 introduced some new object types, object attributes and data types. Tal tried to expand the old RoboFab to cover it, but the old code was not flexible enough. It was very difficult to subclass which made environment specific implementations more difficult than it should have been. It had a huge number of FontLab specific hacks imbedded in places that they shouldn't be. It had so much cruft that it was hard to navigate. Making it work with UFO 3 was not feasible.

We're going to have to start over. Script portability is crucial for type designers. It's also beneficial to the developers of font editors as they won't have to spend time developing a friendly scripting API and it will lower the resistance to change among potential customers.

## Why not call this RoboFab?

This will not be 100% backwards compatible with Robofab. It's going to be backwards compatible with the "important parts" of RoboFab. So, calling it *RoboFab* would lead to a lot of confusion. We're calling this *fontParts* because that's what it is. It's a collection of objects that represent the parts of fonts. Also, by giving it a new name, RoboFab can remain accessible during the transition.

## noneLab?

[![Build Status](https://api.travis-ci.org/robofab-developers/fontParts.svg?branch=master)](https://travis-ci.org/robofab-developers/fontParts)

NoneLab is an example implementation of FontParts for running on the command line. It is built on top of [defcon](https://github.com/typesupply/defcon). The Travis testing is testing this implementation.

## Testing

Tests can be run using the [`py.test`](http://pytest.org/latest/) library. To set up the test suite to run locally, run the following commands:

```bash
cd ~/path/to/fontParts
pip install -e .
py.test
```

You can also run all tests against various versions of Python using [`tox`](https://tox.readthedocs.org/en/latest/). You will need to have several Python's installed: `python2.6`, `python2.7`, `python3.4`, and `pypy`. Consider using [`pyenv`](https://github.com/yyuu/pyenv) to install each version. For example (check what the most recent versions to install with `pyenv install --list`)

```bash
pyenv install 2.6.9
pyenv install 2.7.10
pyenv install 3.4.3
pyenv install pypy-4.0.1

# Creates executables for each of the installed versions
pyenv global system 2.7.10 3.4.3 2.6.9 pypy-4.0.1

# Run the test suite
tox
```
