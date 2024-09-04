from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    
    '''
    This function is used for fetchinng the requirement list 
    '''
    DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
        
        if DOT in requirements:
            requirements.remove(DOT)
    
    return requirements
        
    

setup(
    name='ML project',
    version='0.0.1',
    author='Naman',
    author_email='namankumar4499@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)