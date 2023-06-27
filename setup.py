from setuptools import find_packages,setup
from typing import list 

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list[str]:
    requiremets = []
    with open(file_path) as file_obj:
        requiremets = file_obj.readlines()
        requiremets = [req.replace("\n","") for req in requiremets]
        
        if HYPEN_E_DOT in requiremets:
            requiremets.remove(HYPEN_E_DOT)

    return requiremets



setup(
    name = "Regressor project",
    version = '0.01',
    author = 'nag',
    author_email = 'nag624@gmail.com',
    install_requires = get_requirements('requirements.txt'),
    packages=find_packages()


)