import os
from setuptools import setup, find_packages
from src.version import __VERSION__
with open("README.md", "r") as fh:
    long_description = fh.read()

#https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version
def read(rel_path):
    # type: (str) -> str
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()

def get_version(rel_path):
    # type: (str) -> str
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

setup(
    name='pipelinename',
    # _version.py is created by the build script, if executing this manually either run the build script 
    # or create a _version.py in this folder with the content "__version__='0.0.0'"
    version=__VERSION__,
    description='pipelinename',
    url='https://bitbucket.honeywell.com/projects/HGZAGTDZ/repos/pipelinename/browse',
    author='John.Doe@Honeywell.com',
    keywords='',
    packages=find_packages(),
    # install_requires=['fastapi', 'gunicorn', 'coverage'],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points = {
        'console_scripts': ['main_task=app.pyspark_demo:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Not Approved :: Honeywell",
        "Operating System :: OS Independent",
    ],)