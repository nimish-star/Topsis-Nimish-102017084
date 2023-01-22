import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Nimish-102017084-Topsis",
    version="1.0.1",
    description="Calculates TOPSIS on the given dataset!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/nimish-star/Topsis-Nimish-102017084",
    author="Nimish Lakhmani",
    author_email="nimishlakhmani@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["Topsis"],
    include_package_data=True,
    install_requires=['pandas'],
    entry_points={
        "console_scripts": [
            "Topsis=Topsis.__main__:main",
        ]
    },
)