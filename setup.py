from setuptools import setup, find_packages

setup(
    name='scipcffi',
    version='0.0.0dev0',
    description='Python wrapper for SCIP solver',
    author='Robert Schwarz',
    author_email='mail@rschwarz.net',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    install_requires=['cffi'],
)
