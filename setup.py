import setuptools
"""" lambda-JonRivera - a collection of  Data Science helpter functions """  
"""
lambdata - a collection of Data Science helper functions
"""


REQUIRED = [
    "pandas>=1.1.0",
]

with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()

setuptools.setup(
    name="lambdata-JonRivera",
    version="0.1.0",
    author="JonRivera",
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/JonRivera/Package_Repo",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)