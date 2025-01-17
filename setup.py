from setuptools import setup, find_packages

setup(
    name="auto_clicker",
    version="1.0.0",
    description="A simple auto-clicker with logging.",
    author="João Fernandes",
    author_email="jopedros@ipvc.com",
    packages=find_packages(),
    install_requires=[
        "pynput",
    ],
    entry_points={
        "console_scripts": [
            "auto_clicker=auto_clicker.clicker:main",
        ],
    },
)
