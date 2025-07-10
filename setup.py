### Info like version, author, etc.

'''
The setup.py file is used to package and distribute Python projects.
It contains metadata about the project, such as its name, version, author, and description.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    
    '''
    This function returns a list of requirements from the requirements.txt file.
    It removes any empty lines and comments.
    '''
    
    requirements_list:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from files
            lines = file.readlines()
            ## Process each line
            for line in lines :
                requirement = line.strip()
                ### Ignore empty lines and -e.
                if requirement and requirement != '-e.' :
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt files is not found")
        
    return requirements_list

setup(
    name = "Network Security",
    version= "0.0.1", 
    author = "Yashwanth Krishna Devendran",
    author_email= "yashwanth23110541@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements()
)