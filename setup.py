#can make my ML /application model as a package and use smwhere else and even deploy it in Pypi
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirement(file_path:str)-> List[str]:
    '''this will read the requirement file and give a list of all requirments in the file'''
    requirement=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()   #read all the lines but with each new line it also read a '\n'
        requirements = [req.replace('\n',' ') for req in requirements]   # so here we remove it by space
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
setup(
    name='mlproject',
    version='0.0.1',
    author='Aditya',
    aurthor_email='adityarajsri27@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement("requirments.txt")
)