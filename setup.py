from setuptools import setup, find_packages
from typing import List

hyphen_e_dot="-e ."

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirement
    
    """

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements


from setuptools import setup, find_packages

setup(
    name="MLProjectAWS",
    version="1.0",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)