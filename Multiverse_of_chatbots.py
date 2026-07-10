import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Multiverse Chatbot",
    page_icon="🌌",
    layout="centered"
)

st.title("🌌 THE MULTIVERSE OF CHATBOTS")
st.caption("Choose a personality and start chatting.")

st.markdown("""
<style>

.stApp{
    background:#0f172a;
}

h1{
    text-align:center;
    color:white;
}

[data-testid="stChatMessage"]{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not found in .env file")
    st.stop()

client = genai.Client(api_key=api_key)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("🌌 Multiverse")

    st.write("Choose your favorite personality.")

    st.divider()

    st.write("Powered by Gemini 2.5 Flash")

    st.divider()

    st.write("Made by Biswajith")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# Personality Selection
# -----------------------------
personality = st.selectbox(
    "Who do you want to talk to?",
    [
        "Virat Kohli",
        "Cristiano Ronaldo",
        "Tony Stark",
        "Sherlock Holmes",
        "Batman",
        "Naruto Uzumaki",
        "Steve Jobs",
        "A Senior Google Software Engineer"
    ]
)

greetings = {
    "Tony Stark": "Well... another genius wants my advice?",
    "Batman": "I'm listening.",
    "Naruto Uzumaki": "Believe it! Let's do this!",
    "Sherlock Holmes": "Interesting. Tell me everything.",
    "Virat Kohli": "Let's dominate today!",
    "Cristiano Ronaldo": "Hard work starts now. SIUUUU!",
    "Steve Jobs": "Innovation begins with a simple idea.",
    "A Senior Google Software Engineer":
        "Let's build software the right way."
}

st.info(greetings[personality])

# -----------------------------
# Personality Prompts
# -----------------------------
character_prompts = {

    "Virat Kohli":
    """
You are Virat Kohli.

Speak confidently.
Be energetic.
Talk like a champion.
Motivate people.
Never break character.
""",

    "Cristiano Ronaldo":
    """
You are Cristiano Ronaldo.

Be disciplined.
Talk about hard work.
Use confidence.
Occasionally say "Siuuu!"
Never break character.
""",

    "Tony Stark":
    """
You are Tony Stark.

Be witty.
Be sarcastic.
Be extremely intelligent.
Crack clever jokes.
Never break character.
""",

    "Sherlock Holmes":
    """
You are Sherlock Holmes.

Think logically.
Observe every detail.
Deduce before answering.
Speak like the world's greatest detective.
""",

    "Batman":
    """
You are Batman.

Be serious.
Keep answers short.
Protect Gotham.
Remain mysterious.
Never break character.
""",

    "Naruto Uzumaki":
    """
You are Naruto Uzumaki.

Be cheerful.
Encourage people.
Believe in friendship.
Never give up.
Say 'Believe it!' occasionally.
""",

    "Steve Jobs":
    """
You are Steve Jobs.

Think differently.
Talk about innovation.
Value simplicity.
Inspire creativity.
""",

    "A Senior Google Software Engineer":
    """
You are a Staff Software Engineer at Google.

Explain concepts clearly.
Follow industry best practices.
Think about scalability.
Mentor the user like a senior engineer.

If coding is requested,
explain the approach first,
then provide clean code.
"""
}

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Input
# -----------------------------
user_message = st.chat_input("Type your message...")

if user_message:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_message)

    # Build conversation history
    history = ""

    for message in st.session_state.messages:
        role = "User" if message["role"] == "user" else "Assistant"
        history += f"{role}: {message['content']}\n"

    # Final Prompt
    prompt = f"""
{character_prompts[personality]}

Rules:
- Stay completely in character.
- Never mention you are an AI.
- Continue the conversation naturally.

Conversation History:
{history}

Assistant:
"""

    # Generate Response
    with st.spinner("🌌 Connecting to the Multiverse..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        ai_reply = response.text

    # Save AI response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_reply)