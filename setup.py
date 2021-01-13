from pathlib import Path

from setuptools import setup

project_dir = Path(__file__).parent.absolute()

with open(project_dir / "README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="kdtree-python",
    packages=["kdtree"],
    version="0.2.2",
    description="Implementation of a multidimensional binary search tree for associative searching",
    author="Alessio Sanfratello",
    url="https://github.com/alesanfra/kdtree",
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Intended Audience :: Science/Research",
    ],
)
