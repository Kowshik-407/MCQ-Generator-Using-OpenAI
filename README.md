# MCQ-Generator-Using-OpenAI
Automated MCQ Generator Using Langchain OpenAI_API

## Pre-requisites
  - Install Anaconda and Python 3.8 in local system / Google Colab with Python to be installed
  - VS Code
  - If Anaconda is used the below are required:
	  - Create a Virtual environment and activate it
	  - Install all the packages in the Virutal Environment
   
## Project Creation
**Process:**
  - Setting up the Development Environment in VSCode
  - Few experiments in Anaconda Notebook
  - Coverting the Anaconda Notebook code into Modular Code
  - Creation of WebAPI using Streamlit

**Execution:**
1. Download this ZIP file
2. Open Terminal in VSCode, then execute the below commands:
- Creation of Virtual Environment
```
conda create -p mcq_env python=3.8 -y
```
- Activate the environment
```
source activate ./mcq_env
```
3. Create a .env file and add the OPENAI_API = "<key>"
4. Setup the requirements
```
pip install -r requirements.txt
```
5. Execute the webapp in the terminal
```
streamlit run StreamlitAPP.py
```
