#
# Package structure sourced from:
#   https://waylonwalker.com/minimal-python-package/
# 
from setuptools import setup, find_packages

name="argsy"

setup(
    name=name,
    author='Matt Wiley',
    version="0.0.0",
    description='Tiny wrapper for Python\'s `argparse` package with YAML-based cli configuration.',
    long_description=open('README.md').read() or None,
    long_description_content_type="text/markdown",
    py_modules=[name],
    install_requires=[
        "PyYAML>=5.4.1"
    ],
)