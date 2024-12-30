from setuptools import setup, find_packages

setup(
    name="phonex",
    version="1.0-alpha",
    description="A Python script to search for phone numbers across web pages and files using Google Dorks",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="forria",
    author_email="forria@forria64.space",
    url="https://github.com/forria64/phonex",
    packages=find_packages(),
    install_requires=[line.strip() for line in open("requirements.txt")],
    entry_points={
        "console_scripts": [
            "phonex=phonex.phonex:main",
        ],
    },
    extras_require={
        "dev": ["behave"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

