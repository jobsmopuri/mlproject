from setuptools import find_packages,setup
from typing import List

HYPON_E_DOT="-e ."


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPON_E_DOT in requirements:
            requirements.remove(HYPON_E_DOT)
            
    return requirements
    
    
setup(
    name="mlproject",
    version="0.0.1",
    author="Siva Mopuri",
    author_email="jobs.mopuri@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
    
)