import setuptools

# Read the content of the README file	
with open('README.md', encoding='utf-8') as f:	
    long_description = f.read()	

setuptools.setup(
    name="test_pkg_hmoazam",
    version="0.0.0",
    author="Hanna",
    description="Do not use",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=["test_pkg_hmoazam"]
)