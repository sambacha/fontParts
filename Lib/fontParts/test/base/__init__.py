import unittest
from fontParts.test.base import test_anchor

def testEnvironment(objectProvider):
	modules = [
		("Anchor", test_anchor)
	]
	loader = unittest.TestLoader()
	for name, module in modules:
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
