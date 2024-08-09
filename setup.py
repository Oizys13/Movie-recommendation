from setuptools import setup 

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

AUTHOR_NAME = 'Bourrich Mohamed Reda'
SRC_REPO = 'src'
REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='1.0',
    author=AUTHOR_NAME,
    author_email='brchreda@gmail.com',
    description='A simple python package for movie recommendation system',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package=[SRC_REPO],
    python_requires='>=3.7',
    install_requires=REQUIREMENTS,
)