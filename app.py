
import streamlit as st
from persona import detect_persona
from kb import get_kb_response
from escalation import should_escalate
from llm import generate_response

st.title("Persona-Adaptive Customer Support Agent")

if "turns" not in st.session_state:
    st.session_state.turns = 0

user_message = st.text_input("Customer Message")

if st.button("Send"):
    st.session_state.turns += 1

    persona = detect_persona(user_message)
    kb_response = get_kb_response(user_message)

    if should_escalate(persona, user_message, st.session_state.turns):
        st.error("Escalated to human agent.")
        st.write("Persona:", persona)
        st.write("Issue Summary:", user_message)
    else:
        reply = generate_response(persona, kb_response, user_message)
        st.success(reply)
        st.write("Detected Persona:", persona)