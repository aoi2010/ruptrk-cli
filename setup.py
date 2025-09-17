from setuptools import setup, find_packages
from ruptrk_cli import __version__, __author__, __license__, __email__

setup(
    name="ruptrk-cli",
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="RUPTRK CLI - A basic inventory & sales tracker",
    license=__license__,
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aoi2010/ruptrk-cli",
    packages=find_packages(),
    install_requires=["platformdirs"],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "ruptrk-cli=ruptrk_cli.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
