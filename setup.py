from setuptools import setup
from pkg_resources import parse_requirements

with open("requirements.txt") as f:
    requirements = [str(req) for req in parse_requirements(f.read())]

setup(
    name="app",
    version="0.1.0",
    packages=[
        'app'
    ],
    package_dir={"app": "."},
    install_requires=requirements,
)