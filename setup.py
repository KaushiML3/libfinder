from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="libfinder",
    version="0.2.0",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    author="Kaushi Gihan",
    author_email="kaushigihanml@gmail.com.com",
    description="A simple package to check if a Python library is installed in a Jupyter notebook.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KaushiML3/libfinder",  # Replace with your GitHub repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)