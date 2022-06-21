
from setuptools import setup, find_packages

setup(
    name="cro-general-app",
    version="0.2.0",
    install_require=[],
    py_modules=[
        "general"
    ],
    extras_require={
        "dev": [
            "black", "pytest", "mypy"
        ]
    }
)