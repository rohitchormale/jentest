from setuptools import setup, find_packages


setup(
    name="jentest",
    version="0.1",
    packages=find_packages(),
    scripts=[],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'jentest' package, too:
        'jentest': ['*.msg'],
    },

    # metadata for upload to PyPI
    author="Rohit Chormale",
    author_email="rohitchormale@gmail.com",
    description="jentest",
    license="",
    keywords="",
    url="https://rohitchormale.me",

)
