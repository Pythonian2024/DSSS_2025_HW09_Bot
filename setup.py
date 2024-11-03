# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:54:05 2024

@author: abalh
"""

# setup.py
from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1.0",
    description="A simple package for a Math Game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="DSSS_WS2024_Abdulaziz Alhaidari",
    author_email="azez.alhaidari@fau.de",
    url="https://github.com/Pythonian2024/DSSS-WS2024-HW02",  # optional: link to your GitHub repo
    packages=find_packages(),
    install_requires=[],  # dependencies (e.g., `random` is part of Python's standard library, so no extra needed here)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)