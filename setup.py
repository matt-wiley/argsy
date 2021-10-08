#
# Package structure sourced from:
#   https://waylonwalker.com/minimal-python-package/
# 
from setuptools import setup

name="argsy"

setup(
    name=name,
    author='Matt Wiley',
    version=open('version.txt','r').read().strip(),
    py_modules=[name],
    install_requires=open('requirements/runtime.txt','r').read().split('\n'),
)