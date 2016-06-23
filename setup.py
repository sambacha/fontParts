from setuptools import setup

setup(
    name='fontParts',
    version="0.0.1",
    author='Just van Rossum, Tal Leming, Erik van Blokland, others',
    author_email='info@robofab.com',
    packages=[
        'fontParts',
        'fontParts.base',
        'fontParts.nonelab',
        'fontParts.test'
    ],
    url='http://github.com/robofab-developers/fontParts',
    license='LICENSE.txt',
    description='Tools to manipulate font sources',
    long_description='Tools to manipulate font sources',
    install_requires=[],
    package_dir={'': 'Lib'}
)
