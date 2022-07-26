import streamlit as st
from openai_utils import get_leet_code_solution

st.header("Leetcode Question:")
leet_code_question: str = st.text_area(
    "copy and paste your leetcode question here", height=600
)

if st.button("Get Leetcode Solution"):
    leet_code_answer: str = get_leet_code_solution(leet_code_question)
    st.header("Leetcode Answer")
    st.text(leet_code_answer)
