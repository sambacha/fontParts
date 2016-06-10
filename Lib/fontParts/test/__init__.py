# This is out of date. Will update soon.
#
# """
# The test suite is developed to be environment and format
# agnostic. This is done by defining the tests in base classes
# that follow a specific environment interaction protocol.
# Environment developers will implement only the necessary
# parts of the protocol. The cases are defined in a simple
# text format (defined below) within the test classes.
# Environment developers will implement the creation of these
# cases into their object structure as they see fit.
# 
# ############
# Base Classes
# ############
# 
# The base classes are located in `fontParts.test.base.*`.
# 
# ==============
# Test Structure
# ==============
# 
# ::
# 
#     from fontParts.base import FontPartsError
#     from fontParts.test.base.support import parseCaseDefinitions
# 
#     fooCaseDefinitions = \"\"\"
#     # case definitions
#     \"\"\"
# 
#     class TestFoo(object):
# 
#         caseDefinitions = parseCaseDefinitions(fooCaseDefinitions)
# 
#         # -----------
#         # Environment
#         # -----------
# 
#         def getCaseObjects(self, id):
#             raise NotImplementedError
# 
#         # Other universal methods for resetting,
#         # closing, etc. may be defined here.
# 
#         # --------------
#         # Section Header
#         # --------------
# 
#         def test_bar(self):
#             # Code for testing the bar attribute.
# 
#         def test_changeSomething(self):
#             # Code for testing the changeSomething method.
# 
# ================
# Test Definitions
# ================
# 
# The test definitions should be developed by following
# the `FontParts API documentation <http://fontparts.readthedocs.io/en/latest/index.html>`.
# These break down into two categories.
# 
# #. attributes
# #. methods
# 
# These will be covered in detail below. In general follow
# these guidelines when developing 
# 
# #. Keep the test focused on what is relevant to what
#    is being tested. Don't test file saving within an
#    attribute test in a sub-sub-sub-sub object.
# #. Make the tests as atomic as possible. Don't modify
#    lots of parts of an object during a single test.
#    That makes the tests very hard to debug.
# #. Keep the code clear and concise so that it is easy
#    to see what is being tested. Add documentation
#    to clarify anything that is ambiguious. Try to
#    imagine someone trying to debug a failure of this
#    test five years from now. Will they be able to
#    tell what is going on in the code?
# #. If testing an edge case, make notes defining where
#    this situation is happening, why it is important
#    and so on. Edge case tests often are hyper-specific
#    to one version of one environment and thus have
#    a limited lifespan. This needs to be made clear
#    for future reference.
# #. Test valid and invalid input. The base implementation's
#    validators define what is valid and invalid. Use this
#    as a reference.
# 
# Testing Attributes
# ------------------
# 
# Attribute testing use the method name structure ``test_attributeName``.
# If more than one method is needed due to length or
# complexity, the additional methods use the name
# structure ``test_attributeNameDescriptionOfWhatThisTests``.
# 
# ::
# 
#     def test_bar(self):
#         caseObjects = self.getCaseObjects("some test case")
#         foo = caseObjects["foo"]
#         # get
#         self.assertEqual(
#             foo.bar,
#             "barbarbar"
#         )
#         # set: valid data
#         foo.bar = "heyheyhey"
#         self.assertEqual(
#             foo.bar,
#             "heyheyhey"
#         )
#         # set: invalid data
#         with self.assertRaises(FontPartsError):
#             foo.bar = 123
# 
#     def test_barSettingNoneShouldFail(self):
#         caseObjects = self.getCaseObjects("some test case")
#         foo = caseObjects["foo"]
#         with self.assertRaises(FontPartsError):
#             foo.bar = None
# 
# Getting
# ^^^^^^^
# 
# When testing getting an attribute, test the following:
# 
# * All valid return data types. Use the case definitions
#   to specify these.
# * (How should invalid types be handled? Is that completely
#   the responsibility of the environment?)
# 
# Setting
# ^^^^^^^
# 
# When testing setting an attribute, test the following:
# 
# * All valid input data types. For example if setting
#   accepts a number, test int and float. If pos/neg
#   values are allowed, test both.
# * A representative sample of invalid data types/values.
# 
# If an attribute does not support setting, it should
# be tested to make sure that an attempt to set raises
# the appropriate error.
# 
# Testing Methods
# ---------------
# 
# Testing methods should be done atomically, modifying
# a single argument at a time. For example, if a method
# takes x and y arguments, test each of these as
# independently as possible. The following should be
# tested for each argument:
# 
# * All valid input data types. For example if setting
#   accepts a number, test int and float. If pos/neg
#   values are allowed, test both.
# * A representative sample of invalid data types/values.
# 
# ::
# 
#     def test_changeSomething(self):
#         caseObjects = self.getCaseObjects("some test case")
#         bar = caseObjects["bar"]
#         bar.changeSomething(x=100, y=100)
#         self.assertEqual(
#             bar.thing,
#             (100, 100)
#         )
#         with self.assertRaises(FontPartsError):
#            bar.changeSomething(x=None, y=100)
#         with self.assertRaises(FontPartsError):
#            bar.changeSomething(x=100, y=None)
# 
# ================
# Case Definitions
# ================
# 
# Test cases are defined with text descriptions. The descriptions
# are defined with a set of commands and object data expressed in
# the fontParts API. ::
# 
# ::
# 
#     >>>
#     + id: Generic Foo
#     + object: Foo = myFoo
#     myFoo.name = None
#     myFoo.x = 1
#     myFoo.y = 2
#     <<<
# 
#     >>>
#     + base: Generic Foo
#     + id: Test Foo 1
#     myFoo.name = "testFoo1"
#     <<<
# 
# These are the keywords and tokens (whitespace as shown is required):
# 
# * # indicates a comment. Any text after the token is ignored.
# * ``>>>`` indicates the start of a case definition.
# * ``<<<`` indicates the end of a case definition.
# * ``+ base: Some Text`` defines a case to use as the base for this case.
#   This allows for reuse of objects for brevity and consistency. Any changes
#   to the base must be defined after the ``base`` declaration.
# * ``+ id: Some Text`` defines the case id.
# * ``+ object: Class = objectID`` defines an object to create.
#   ``Class`` is the class name being referenced. ``objectID`` is the
#   identifier for the object. More than one of these is allowed.
# 
# If a line does not match one of these, it is considered a description
# of the case. These descriptions follow the fontParts API.
# 
# 
# ##########################
# Environment Implementation
# ##########################
# 
# The environment specific implementations of the
# tests are created by subclassing the base tests,
# mixing in unittest.TestCase and implementing the
# environment interaction protocols. ::
# 
#     class TestMyAppFoo(TestFoo, unittest.TestCase):
# 
#         def getCaseObjects(self, id):
#             caseDefinition = self.caseDefinitions[id]
#             return self.whatever.something.makeTestObjects(caseDefinition)
# 
# The case definitions are stored within the base test
# classes in a dict keyed by the case id with a dict of
# the following form as the value::
# 
# {
#     "objects" : {
#         "objectID" : "class name"
#     },
#     "description" : "text description"
# }
# 
# The `getCaseObjects` method is expected to return the
# a dictionary of objects created with the appropriate
# classes and populated with the data defined in the
# description. This dictionary must be keyed with the
# object ids.
# """

import unittest
from fontParts.test import test_anchor

def testEnvironment(objectProvider):
  modules = [
    test_anchor
  ]
  loader = unittest.TestLoader()
  for module in modules:
    suite = loader.loadTestsFromModule(module)
    _setObjectProvider(suite, objectProvider)
    runner = unittest.TextTestRunner()
    runner.run(suite)

def _setObjectProvider(suite, objectProvider):
  for i in suite:
    if isinstance(i, unittest.TestSuite):
      _setObjectProvider(i, objectProvider)
    else:
      i.objectProvider = objectProvider
