from setuptools import find_packages, setup

setup(
    name='mcqgenerator', 	# Name of the package
    version='0.0.1', 		# Version of the package
    author='Kowshik Kumar Aitha',
    author_email='kowshikkumaraitha@gmail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)