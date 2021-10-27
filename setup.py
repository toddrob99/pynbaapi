import setuptools
from pynbaapi.__version__ import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pynbaapi",
    version=__version__,
    author="Todd Roberts",
    author_email="todd@toddrob.com",
    description="NBA API Wrapper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/toddrob99/pynbaapi",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
