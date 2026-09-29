"""Setup configuration for group project."""

from setuptools import find_packages, setup


setup(
    name="group-project",
    version="0.1.0",
    description="A group Python project",
    author="Group Team",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=23.0",
            "flake8>=6.0",
        ],
    },
)
