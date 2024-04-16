# app.py
import streamlit as st
from document_reader import read_pdf, read_docx
from openai_utils import extract_information, generate_test_cases, extract_process_names
from pinecone_query import search_for_process_descriptions

st.title('Automated Test Case Generator')

uploaded_file = st.file_uploader("Upload your Functional Specification Document", type=['pdf', 'docx'])
if uploaded_file is not None:
    # Read document based on file type
    if uploaded_file.name.endswith('.pdf'):
        document_text = read_pdf(uploaded_file)
    elif uploaded_file.name.endswith('.docx'):
        document_text = read_docx(uploaded_file)

    # Dynamic process extraction and searching for their details
    process_names = extract_process_names(document_text)
    if process_names:
        process_details = search_for_process_descriptions(process_names)
        for process_name, details in process_details.items():
            st.subheader(f"Details for {process_name}:")
            st.write(details)

    # Extract other information and generate test cases
    extracted_info = extract_information(document_text)
    test_cases = generate_test_cases(extracted_info)
    st.subheader("Extracted Information:")
    st.write(extracted_info)
    st.subheader("Generated Test Cases:")
    st.text(test_cases)
