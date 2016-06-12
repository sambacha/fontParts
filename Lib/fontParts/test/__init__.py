"""
The test suite is developed to be environment and format
agnostic. Environment developers only need to implement
a function that provides objects for testing and a simple
Python script that sends the function to the test suite.

##########################
Environment Implementation
##########################

The main thing that an environment needs to implement is
the test object generator. This should create an object
for the requested class identifier. ::

  def MyAppObjectGenerator(cls):
    obj = myApp.foo.bar.something.hi(cls)
    return obj

The class identifiers are as follows:

* font
* info
* groups
* kerning
* features
* lib
* layer
* glyph
* contour
* segment
* bpoint
* point
* component
* anchor
* image
* guideline

If an environment does not allow orphan objects, it is up
to the environment to retain any necessary parent objects
during testing.

Once an environment has developed this function, all that
remains is to pass the function to the test runner::

  from fontParts.test import testEnvironment

  if __name__ == "__main__":
    testEnvironment(MyAppObjectGenerator)

This can then be executed and the report will be printed.

==============
Important Note
==============

It is up to each environment to ensure that the bridge from
the environment's native objects to the fontParts wrappers
is working properly. This has to be done on an environment
by environment basis since the native objects are not
consistently implemented.


###################
Test Implementation
###################

The test cases are located in ``fontParts.test.test_*``.

==============
Test Structure
==============

::

import unittest
from fontParts.base import FontPartsError

class TestFoo(unittest.TestObject):

    # --------------
    # Section Header
    # --------------

    def getFoo_generic(self):
      # code for building the object

    def test_bar(self):
        # Code for testing the bar attribute.

    def test_changeSomething(self):
        # Code for testing the changeSomething method.


================
Test Definitions
================

The test definitions should be developed by following
the `FontParts API documentation <http://fontparts.readthedocs.io/en/latest/index.html>`.
These break down into two categories.

#. attributes
#. methods

These will be covered in detail below. In general follow
these guidelines when developing 

#. Keep the test focused on what is relevant to what
   is being tested. Don't test file saving within an
   attribute test in a sub-sub-sub-sub object.
#. Make the tests as atomic as possible. Don't modify
   lots of parts of an object during a single test.
   That makes the tests very hard to debug.
#. Keep the code clear and concise so that it is easy
   to see what is being tested. Add documentation
   to clarify anything that is ambiguious. Try to
   imagine someone trying to debug a failure of this
   test five years from now. Will they be able to
   tell what is going on in the code?
#. If testing an edge case, make notes defining where
   this situation is happening, why it is important
   and so on. Edge case tests often are hyper-specific
   to one version of one environment and thus have
   a limited lifespan. This needs to be made clear
   for future reference.
#. Test valid and invalid input. The base implementation's
   validators define what is valid and invalid. Use this
   as a reference.

Testing Attributes
------------------

Attribute testing uses the method name structure ``test_attributeName``.
If more than one method is needed due to length or
complexity, the additional methods use the name
structure ``test_attributeNameDescriptionOfWhatThisTests``.

::

    def test_bar(self):
        foo = self.getFoo_generic()
        # get
        self.assertEqual(
            foo.bar,
            "barbarbar"
        )
        # set: valid data
        foo.bar = "heyheyhey"
        self.assertEqual(
            foo.bar,
            "heyheyhey"
        )
        # set: invalid data
        with self.assertRaises(FontPartsError):
            foo.bar = 123

    def test_barSettingNoneShouldFail(self):
        foo = self.getFoo_barNontShouldFail()
        with self.assertRaises(FontPartsError):
            foo.bar = None

Getting
^^^^^^^

When testing getting an attribute, test the following:

* All valid return data types. Use the case definitions
  to specify these.
* (How should invalid types be handled? Is that completely
  the responsibility of the environment?)

Setting
^^^^^^^

When testing setting an attribute, test the following:

* All valid input data types. For example if setting
  accepts a number, test int and float. If pos/neg
  values are allowed, test both.
* A representative sample of invalid data types/values.

If an attribute does not support setting, it should
be tested to make sure that an attempt to set raises
the appropriate error.

Testing Methods
---------------

Testing methods should be done atomically, modifying
a single argument at a time. For example, if a method
takes x and y arguments, test each of these as
independently as possible. The following should be
tested for each argument:

* All valid input data types. For example if setting
  accepts a number, test int and float. If pos/neg
  values are allowed, test both.
* A representative sample of invalid data types/values.

::

    def test_changeSomething(self):
        bar = self.getBar_something()
        bar.changeSomething(x=100, y=100)
        self.assertEqual(
            bar.thing,
            (100, 100)
        )
        with self.assertRaises(FontPartsError):
           bar.changeSomething(x=None, y=100)
        with self.assertRaises(FontPartsError):
           bar.changeSomething(x=100, y=None)

===================
Objects for Testing
===================

Objects for testing are defined in methods with the name
structure ``getFoo_description``. The base object will be
generated by the environment by calling
``self.objectGenerator("classIdentifier")``. This will return
a fontTools wrapped object ready for population and testing. ::

  def getFoo_generic(self):
    foo = self.objectGenerator("foo")
    foo.bar = "barbarbar"
    return foo

=====
To Do
=====

- Establish tests for pen protocol in test_glyph.

"""

from __future__ import print_function
import unittest
from fontParts.test import test_font
from fontParts.test import test_info
from fontParts.test import test_groups
from fontParts.test import test_kerning
from fontParts.test import test_features
from fontParts.test import test_layer
from fontParts.test import test_glyph
from fontParts.test import test_contour
from fontParts.test import test_segment
from fontParts.test import test_bPoint
from fontParts.test import test_point
from fontParts.test import test_component
from fontParts.test import test_anchor
from fontParts.test import test_image
from fontParts.test import test_guideline


def testEnvironment(objectGenerator):
    modules = [
        test_font,
        test_info,
        test_groups,
        test_kerning,
        test_features,
        test_layer,
        test_glyph,
        test_contour,
        test_segment,
        test_bPoint,
        test_point,
        test_component,
        test_anchor,
        test_image,
        test_guideline
    ]
    loader = unittest.TestLoader()
    for module in modules:
        print()
        print()
        moduleName = module.__name__
        print(moduleName)
        print("-" * 70)

        suite = loader.loadTestsFromModule(module)
        _setObjectGenerator(suite, objectGenerator)
        runner = unittest.TextTestRunner()
        runner.run(suite)

def _setObjectGenerator(suite, objectGenerator):
    for i in suite:
        if isinstance(i, unittest.TestSuite):
            _setObjectGenerator(i, objectGenerator)
        else:
            i.objectGenerator = objectGenerator
