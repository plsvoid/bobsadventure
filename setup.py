"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['./src/bob.py']
DATA_FILES = ['lofiHipHop.mp3','moyai.png','doggy.jpeg','Death.png','start.png']
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
