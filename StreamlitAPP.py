# Import all the necessary packages
import os
import json
import traceback
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain.callbacks import get_openai_callback
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

# Loading json file
with open('/config/workspace/Response.json', 'r') as file: # Load the approp. path
    RESPONSE_JSON = json.load(file)

# Creating a title for the app
st.title("Automated MCQ Generator Application with LangChain 🦜️🔗")

# Create a form using st.form
with st.form("user_inputs"):
    # Upload the file
    uploaded_file = file.uploader("Upload a PDF or text file")

    # Input Fields
    mcq_count = st.number_input("No. of MCQs: ", min_value=3, max_value=50)
    
    # Subject
    subject = st.text_input("Insert Subject: ", max_chars=20)
    
    # Quiz Tone
    tone = st.text_input("Complexity Level of Questions: ", max_chars=20, placeholder="Simple")
    
    # Add Button
    button = st.form_submit_button("Create MCQs")
    
    # Check if the button is clicked and all the fields have input or not
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Loading...."):
            try:
                text = read_file(uploaded_file)
                # Count the tokens and the cost of API Call
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain({
                    	"text": text,
                    	"number": mcq_count,
                    	"subject": subject,
                    	"tone": tone,
                    	"response_json": json.dumps(RESPONSE_JSON)
                    })
                # st.write(response)
            
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
            
            else:
                print(f"Total Tokens: {cb.total_tokens}")
                print(f"Prompt Tokens: {cb.prompt_tokens}") # Input Tokens
                print(f"Completion Tokens: {cb.completion_tokens}") # Output Tokens
                print(f"Total Cost (USD): ${cb.total_cost}")
        
                if isinstance(response, dict): # The isinstance() function returns True if the specified object is of the specified type, else False.
                    # Extract the quiz data from the response
                    quiz = response.get("quiz", None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1
                            st.table(df)
                            # Display the review in a textbox as well
                            st.text_area(label="Review", value=response["review"])
                        else:
                            st.Error("Error in the table data")
                else:
                    st.write(response)

# Now, for executing this webapplication. Goto the terminal > Git Bash > Current Virtual Environment
# 	streamlit run StreamlitAPP.py
# To give the specified port
# 	streamlit run StreamlitAPP.py --server.port 8080

# Thus, it opens the browser and asks the input: Here, you can experiment via UI and finally you can see the MCQs...
# You are going to view the following:
#   - Upload a PDF or txt file
#   - No. of MCQs
#   - Insert Subject
#   - Complexity Level of Questions
#   - Create MCQs [Button]
#   - Once, it is successful. It shows two boxes: MCQ Dataframe + Review