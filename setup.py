from setuptools import setup, find_packages
from pkg_resources import parse_requirements


with open("requirements.txt") as f:
    requirements = [str(req) for req in parse_requirements(f.read())]

setup(
    name="testapp",
    version="0.1.0",
    package_dir={"": "app"},
    packages=find_packages("testapp"),
    install_requires=requirements,
)