### to create local package we need this setup.py

from setuptools import setup, find_packages

setup(
    name='Generativew AI Project',
    version='0.0.0',
    description='A tool to create interview questions',
    author='Vivek',
    author_email='dalmiagolu@gmail.com',
    packages=find_packages(), ### find all python packages in the current directory __init__.py file
    install_requires=[]
)

              