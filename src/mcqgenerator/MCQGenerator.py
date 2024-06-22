# Migrating the Anaconda notebook code into modular code

# Import all the necessary packages
import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import loggin

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Load env variables
load_dotenv()
key = os.getenv("OPENAI_API_KEY")

# Use ChatOpenAI to use the LLM
llm = ChatOpenAI(openai_api_key=key, model_name="gpt-3.5-turbo", temperature=0.7)

# Creation of quiz_generation_prompt PromptTemplate
TEMPLATE = """
Text: {text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choize questions for the {subject} students in \
{tone} tone. Make sure the questions are not repeated and check all the questions \
to be conforming the text as well. Make sure to format your response like RESPONSE_JSON \
below and use it as a guide.\
Ensure to make {number} of MCQs
### RESPONSE_JSON
{response_json}
"""

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=TEMPLATE
)

# Using the LLMChain to connect the LLM and the PromptTemplate
quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)


# For analyzing the correct answer. Created another template, then giving the template1 output as the template2 input.
EVALUATION_TEMPLATE = """
You are an expert English Grammarian and Writer. Given a Mutliple Choice Quiz for {subject} students. \
You need to evaluate the complexity of the question and give a complte analysis of the quiz. \
Only use at max 50 words for complexity if the quiz is not at per with the cognitive and analytical abilities of the students, \
update the quiz questions which needs to be changed and change the tone such that it perfects fits the student ability.
Quiz_MCQs: {quiz}

Check from an expert English Writer of the above quiz:
"""

quiz_evaluation_prompt = PromptTemplate(
  input_variables=["subject", "quiz"], 
  template=EVALUATION_TEMPLATE
)

# Using again the LLMChain to connect the LLM and the PromptTemplate
review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)


# Now, finally connecting both quiz_chain and review_chain by using SequentialChain
generate_evaluate_chain = SequentialChain(
  chains=[quiz_chain, review_chain],
  input_variables=["text", "number", "subject", "tone", "response_json"],
  output_variables=["quiz", "review"],
  verbose=True
)