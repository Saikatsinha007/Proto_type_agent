import streamlit as st
from orchestrator_agent import OrchestratorAgent
from utils import log_action

API_KEY = "AIzaSyDshoHIAfzoWuPDqX9bvKtuhHotJsdaw2o"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

st.set_page_config(page_title="Multi-Agent Query Handler", layout="centered")

st.title("🧠 Multi-Agent System")

user_input = st.text_area("Enter your query", height=150)

if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = OrchestratorAgent(api_key=API_KEY, base_url=BASE_URL)

if st.button("Submit"):
    if user_input.strip():
        with st.spinner("Processing..."):
            result = st.session_state.orchestrator.handle_query(user_input)
        st.success("Agent Response:")
        st.markdown(f"> {result}")
    else:
        st.warning("Please enter a query.")
