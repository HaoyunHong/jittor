
import setuptools
from setuptools import setup, find_packages
import os

path = os.path.dirname(__file__)
with open(path + "/README.src.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='jittor',  
    version='1.0.0',
    # scripts=[],
    author="Jittor Group",
    author_email="ran.donglang@gmail.com",
    description="a Just-in-time(JIT) deep learning framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://jittor.org",
    # packages=setuptools.find_packages(),
    python_requires='>=3.7',

    packages=["jittor", "jittor.test", "jittor.models", "jittor.utils", "jittor_utils"],
    package_dir={'':path+'/python'},
    package_data={'': ['*', '*/*', '*/*/*','*/*/*/*','*/*/*/*/*','*/*/*/*/*/*']},
    # include_package_data=True,
    install_requires=[
        "pybind11",
        "numpy",
        "tqdm",
        "pillow",
        "astunparse",
    ],
 )