import setuptools

with open("DESCRIPTION.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolmate',
    version='1.0.0.dev1',
    author="Vagner Bessa",
    author_email="bessavagner@gmail.com",
    description="A personal utility package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bessavagner/toolmate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
    'numpy',
    'matplotlib',
    'scipy'
    ]
 )