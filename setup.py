from setuptools import setup, find_packages
from os.path import basename, splitext

setup(
    name="ml_aspanformer",
    packages=find_packages(),
    version="0.1.0",
    author="J",
    install_requires=open("requirements.txt", "r").read().split("\n"),
)
