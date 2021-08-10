from setuptools import setup

long_description = open("README.md", "r").read()

setup(
    name="simpleio",
    packages=["simpleio"],
    version="0.1.0",
    license="MIT",
    description="Simple IO Instructions that convert to assembly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jack Murrow",
    author_email="jack.murrow2005@gmail.com",
    url="https://github.com/jackprogramsjp/simpleio",
    keywords=["Simple", "IO", "Simple IO", "Input Output"],
    entry_points={"console_scripts": ["simpleio = simpleio.simpleio:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
