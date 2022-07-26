from setuptools import find_namespace_packages, setup

setup(
    name="cro-broadcast",
    version="0.3.0",
    install_requires=["flask"],
    package_dir={"": "src"},
    packages=find_namespace_packages(include=["cro.*"]),
    extras_require={"dev": ["black", "pytest", "isort", "mypy", "sphinx"]},
)
