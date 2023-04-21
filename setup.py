from setuptools import setup

setup(
    name="ml-aspanformer",
    packages=["src"],
    version="0.1.0",
    author="J",
    install_requires=open("requirements.txt", "r").read().split("\n"),
)
