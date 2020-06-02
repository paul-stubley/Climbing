from setuptools import setup

with open("pgs_climbing/README.md", "r") as fh:
    long_description = fh.read()

setup(name='pgs_climbing',
      version='0.1',
      description='Classes to describe rock-climbing',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/paul-stubley/Climbing",
      packages=['pgs_climbing'],
      zip_safe=False)