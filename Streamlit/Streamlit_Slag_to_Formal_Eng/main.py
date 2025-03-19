import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

template = """
Below is a draft text that may be poorly worded.
Your goal is to:
- Properly redact the draft text  
- Convert the draft text to a specified tone
- Convert the draft text to a specified dialect

Here are some examples different Tones:
- Formal: Greetings! OpenAI has announced that Sam Altman is rejoining the company as its Chief Executive Officer.
- Informal: Hey everyone, it's been a wild week! We've got some exciting news to share - Sam Altman is back at OpenAI!

Here are some examples of words in different dialects:
- American: French Fries, cotton candy, apartment, garbage, \
    cookie, green thumb, parking lot, pants, windshield
- British: chips, candyfloss, flat, rubbish, biscuit, green fingers, \
    car park, trousers, windscreen

Example Sentences from each dialect:
- American: Greetings! OpenAI has announced that Sam Altman is rejoining the company as its Chief Executive Officer!
- British: On Wednesday, OpenAI, the esteemed artificial intelligence start-up, announced that Sam Altman would...

Please start the redaction with a warm introduction. Add the introduction \
if you need to.

Below is the draft text, tone, and dialect:
DRAFT: {draft}
TONE: {tone}
DIALECT: {dialect}

YOUR {dialect} RESPONSE:
"""

#PromptTemplate variables definition
prompt = PromptTemplate(
    input_variables=["draft", "tone", "dialect"],
    template=template,
)

#LLM Key Loading and Function

def load_LLM(openai_api_key):
    """Logic to load the chain you want to use goes here."""
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm

# Page title and header
st.set_page_config(page_title="Re-Write your text")
st.header("Re-Write your text")


#Intro
col1,col2 = st.columns(2)

with col1:
    st.markdown("Re-write your text in different styles")

with col2:
    st.write("Subscribe to our [newsletter](https://www.example.com) for more updates")

#Input OpenAI API Key

st.markdown("## Enter your OpenAI API Key")

def get_openai_api_key():
    input_text = st.text_input(label="OPENAI API KEY", placeholder="Enter your OpenAI API Key" , key="openai_api_key_input", type="password")
    return input_text

openai_api_key = get_openai_api_key()

# Input

st.markdown("## Enter your text you want to re-write")

def get_draft():
    draft_text = st.text_area(label="Text", key="draft_input", label_visibility="collapsed", placeholder="Enter your text here")
    return draft_text

draft_input = get_draft()

if len(draft_input.split(" ")) > 700:
    st.write("Please enter a text with less than 700 words")
    st.stop()

# Prompt Template 
# Prompt template tuning options
col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox(
        'Which tone would you like your redaction to have?',
        ('Formal', 'Informal'))

with col2:
    option_dialect = st.selectbox(
        'Which English Dialect would you like?',
        ('American', 'British'))

# Output
st.markdown("### Your Re-written text:")

if draft_input:
    if not openai_api_key:
        st.warning('Please insert OpenAI API Key. \
            Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)',
            icon="⚠️")
        st.stop()

    llm = load_LLM(openai_api_key=openai_api_key)

    prompt_with_draft = prompt.format(
        tone=option_tone,
        dialect=option_dialect,
        draft=draft_input
    )


    improved_redaction = llm(prompt_with_draft)

    st.write(improved_redaction)