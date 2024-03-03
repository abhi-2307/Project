from setuptools import find_packages,setup
from typing import List

const='-e .'
def get_requirements(file_path)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if const in requirements:
            requirements.remove(const)
    return requirements              

    

setup(
    name = 'ML_project',
    version = '0.0.1',
    author = 'Abhi',
    author_email = 'abhidevkonigeti2003@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)