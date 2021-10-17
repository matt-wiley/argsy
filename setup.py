#
# Package structure sourced from:
#   https://waylonwalker.com/minimal-python-package/
# 
from setuptools import setup

name="argsy"

setup(
    name=name,
    author='Matt Wiley',
    version="0.0.0",
    py_modules=[name],
    install_requires=open('requirements/runtime.txt','r').read().split('\n'),
)