from setuptools import setup

setup(
    name="ml_aspanformer",
    packages=["ml-aspanformer"],
    version="0.1.0",
    author="J",
    install_requires=open("requirements.txt", "r").read().split("\n"),
)
