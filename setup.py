from setuptools import setup, find_packages

setup(
    name="gh-peeker",
    version="0.0.1",
    author="Sattwik Sahu",
    author_email="sahusattwik@gmail.com",
    url="https://github.com/gitwikc/gh-peeker",
    description="An application that allows you to peek at repos created by GitHub users",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "requests", "colorama"],
    entry_points={"console_scripts": ["ghpeek = src.__main__:main"]},
)
