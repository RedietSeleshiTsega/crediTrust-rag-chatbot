import streamlit as st
from rag_pipeline import generate_answer

st.set_page_config(page_title="CrediTrust Complaint Bot", layout="wide")

st.title("📋 CrediTrust Complaint Chatbot")
st.write("Ask me anything about customer complaints (BNPL, Loans, Transfers, etc.)")

question = st.text_input("💬 Your Question:")

if st.button("Get Answer") and question:
    with st.spinner("Generating answer..."):
        answer, sources, metadata = generate_answer(question)
        st.success(answer)
        st.markdown("**Sources:**")
        for src in sources:
            st.markdown(f"- {src}")
