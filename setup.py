from setuptools import setup, find_packages

setup(
    name="lmutils",
    version="0.99b",
    packages=find_packages(),
    install_requires=["prettyprint", "getpass4", "pyyaml", "tabulate", "icecream"],  # Add dependencies here
    author="yuke1922",
    description="Dumb Python functions",
)
