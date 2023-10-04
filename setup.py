from setuptools import setup, find_packages
from typing import List

def get_requirenment(file_path:str)->List[str]:
    '''this will return list of requirenments'''
    requirenment=[]
    with open(file_path) as file_obj:
        requirenment=file_obj.readlines()
        requirenment=[req.replace('\n',"") for req in requirenment]
        return requirenment





setup(
    name='sumit',
    version='0.1.0',
    description='this is practice project for me',
    author='sumit',
    author_email='sumitnsawant822@gmail.com',
    package=find_packages(),
    import_requires=get_requirenment('requirenment.txt')
    )