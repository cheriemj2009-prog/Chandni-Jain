import streamlit as st
import google.generativeai as genai

genai.configure(api_key="PASTE_YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

st.title("Bloom’s Taxonomy Checker")

question = st.text_area("Enter your question:")

if st.button("Analyze Question"):
    prompt = f"""
    Classify the following question according to Bloom's Taxonomy
    (Remember, Understand, Apply, Analyze, Evaluate, Create).
    Then suggest how to rephrase it to a higher cognitive level.

    Question: {question}
    """

    response = model.generate_content(prompt)
    st.subheader("AI Analysis")
    st.write(response.text)
