from setuptools import find_packages,setup



setup(
    name='mcqgenerator',
    version='0.0.1',
    author='utkarsh',
    install_requires= ['openai','streamlit','python-dotenv','PyPDF2','langchain-community'],
    packages=find_packages()

)