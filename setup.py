from setuptools import setup, find_packages
from os.path import join, dirname

import cvi

setup(
    name='cvi',
    version=cvi.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=[
        'opencv-python',
        'opencv-contrib-python',
    ],
)
