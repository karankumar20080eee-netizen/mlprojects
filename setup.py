from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open (file_path) as fil_obj:
        requirements=fil_obj.readlines()   
        requirements=[req.rplace("\n"," ")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements        
setup(
name="mlprojects",
version="0.0.1",
author="karan",
packages=find_packages(),
install_requires=get_requirements("requirements.txt"),    
    
    
    
    
)