from setuptools import setup

setup(
    name="ml-aspanformer",
    packages=["ml-aspanformer"],
    version="0.1.0",
    package_dir={'':'src'},
    author="J",
    install_requires=open("requirements.txt", "r").read().split("\n"),
)
