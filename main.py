import streamlit as st
from multiagents import agent_team
from agno.agent import Agent

st.set_page_config(page_title="AI Analyst Chat", page_icon="🤖", layout="centered", initial_sidebar_state="collapsed")

# Custom dark mode styling
st.markdown(
    """
    <style>
    body, .stApp { background: #000 !important; color: #fff !important; }
    .stTextInput > div > div > input, .stTextArea > div > textarea {
        background: #111 !important; color: #fff !important; border-radius: 1.5em !important;
    }
    .stButton > button { background: #fff !important; color: #000 !important; border-radius: 1.5em !important; }
    .stChatMessage { background: #18181b !important; color: #fff !important; border-radius: 1.5em !important; margin-bottom: 0.5em; padding: 1em; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 AI Analyst Chat")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Display chat history
for msg in st.session_state['messages']:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

user_input = st.chat_input("Type your message...")
if user_input:
    # Show user message
    st.session_state['messages'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.markdown(user_input)
    # Get agent response
    with st.spinner('Thinking...'):
        response = agent_team.run(user_input)
    st.session_state['messages'].append({'role': 'assistant', 'content': response})
    with st.chat_message('assistant'):
        st.markdown(response)
