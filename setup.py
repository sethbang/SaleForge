from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Generate fake sales data'
LONG_DESCRIPTION = 'A package that allows you to generate fake sales data for data science projects.'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="SaleForge",
    version=VERSION,
    author="Seth Bangert",
    author_email="seth@sbang.me",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'sale', 'data', 'fake', 'random', 'data science'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ]
)
