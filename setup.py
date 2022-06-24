from setuptools import setup, find_packages

setup(
    name="cro-general-app",
    version="0.3.0",
    install_require=["flask"],
    package_dir={"": "src"},
    packages=find_packages(),
    extras_require={"dev": ["black", "pytest", "mypy"]},
)
