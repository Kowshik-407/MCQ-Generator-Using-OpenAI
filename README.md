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
3. Create a .env file and add the below line:
```
OPENAI_API = "<key>"
```
4. Setup the requirements
```
pip install -r requirements.txt
```
5. Execute the webapp in the terminal
```
streamlit run StreamlitAPP.py
```

## Website Overview
#### Home Page
![image](https://github.com/Kowshik-407/MCQ-Generator-Using-OpenAI/assets/66817358/14e54bf1-bd49-4111-aad1-3f58b7b02e9b)


#### Working with Webapp
![mcqgenerator-gif](https://github.com/Kowshik-407/MCQ-Generator-Using-OpenAI/assets/66817358/f9a16c6f-66c1-41a1-b22c-d2579eb784eb)
![image](https://github.com/Kowshik-407/MCQ-Generator-Using-OpenAI/assets/66817358/355ab37c-ac27-48fe-ad3e-f3c11ece1b13)
![image](https://github.com/Kowshik-407/MCQ-Generator-Using-OpenAI/assets/66817358/be7012b5-52f5-4005-a44e-a86c0b8be1e2)

