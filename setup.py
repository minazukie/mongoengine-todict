import io
import os
import re

from setuptools import setup, find_packages


def read(*filenames, **kwargs):
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", os.linesep)
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


def read_version():
    content = read(os.path.join(os.path.dirname(__file__), "mongoengine_todict", "__init__.py"))
    return re.search(r"__version__ = \"([^']+)\"\n", content).group(1)


setup(
    name="mongoengine_todict",
    version=read_version(),
    packages=find_packages(),
    license="MIT",
    author="minazukie",
    url="https://github.com/minazukie/mongoengine-todict",
    author_email="minazukie2015@gmail.com",
    description="Mongoengnine document to Python dict plugin",
    install_requires=[],
    test_suite=None,
    tests_require=[],
)
