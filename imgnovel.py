import streamlit as st
import os
import json
import requests
from gtts import gTTS
import uuid

from PIL import Image
from io import BytesIO

from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(
    page_title="AI Visual Novel",
    page_icon="🎮",
    layout="wide"
)

if "chat" not in st.session_state:
    st.session_state.chat = None

if "history" not in st.session_state:
    st.session_state.history = []

if "story" not in st.session_state:
    st.session_state.story = ""

if "image" not in st.session_state:
    st.session_state.image = None

if "options" not in st.session_state:
    st.session_state.options = []

if "image_prompt" not in st.session_state:
    st.session_state.image_prompt = ""

if "audio_file" not in st.session_state:
    st.session_state.audio_file = None

@st.cache_resource
def get_gemini_client():
    return genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

client = get_gemini_client()

SYSTEM_PROMPT = """
You are an AI Visual Novel Engine.

Always reply ONLY with valid JSON.

Do not use markdown.

Do not wrap the response inside ```.

Return ONLY this structure:

{
    "story_text": "",
    "image_prompt": "",
    "options": [
        "",
        "",
        ""
    ]
}

Rules:

The image_prompt must be a professional AI image generation prompt.

Always include:

masterpiece,
best quality,
8k,
cinematic,
highly detailed,
dramatic lighting,
concept art,
beautiful composition,

followed by a detailed description of the current scene.

Do not include quotation marks.
"""

st.title("🎮 AI Multi-Modal Visual Novel")
st.caption("Create your own adventure powered by Gemini + Pollinations AI")
with st.sidebar:
    st.title("⚙️ Story Settings")

    genre = st.selectbox(
        "Story Genre",
        [
            "Fantasy",
            "Sci-Fi",
            "Adventure",
            "Mystery",
            "Horror"
        ]
    )

    art_style = st.selectbox(
        "Art Style",
        [
            "Anime",
            "Photorealistic",
            "Sketch",
            "3D Render",
            "Oil Painting"
        ]
    )

    start_story = st.button("🚀 Start Story")

story_container = st.container()

image_container = st.container()

audio_container = st.container()

choices_container = st.container()

with story_container:
    st.subheader("📖 Story")

    if st.session_state.story:
        st.write(st.session_state.story)
    else:
        st.info("Click **Start Story** to begin your adventure.")

with image_container:

    st.subheader("🖼️ Scene")

    if st.session_state.image:

        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:
            st.image(
                st.session_state.image,
                width=700
            )

    else:

        st.info("Scene image will appear here.")

with audio_container:

    st.subheader("🔊 Narration")

    if st.session_state.audio_file:

        st.audio(st.session_state.audio_file, format="audio/mp3")

    else:

        st.info("Narration will appear here.")

with choices_container:

    st.subheader("🎯 Choices")

    if st.session_state.options:

        for option in st.session_state.options:

            if st.button(option, use_container_width=True):

                try:

                    response = st.session_state.chat.send_message(option)

                    data = json.loads(response.text)

                    st.session_state.story = data["story_text"]

                    st.session_state.image_prompt = data["image_prompt"]

                    st.session_state.options = data["options"]

                    # Generate Image
                    try:

                        image_url = (
                            f"https://image.pollinations.ai/prompt/"
                            f"{st.session_state.image_prompt}"
                        )

                        image_response = requests.get(image_url)

                        image = Image.open(BytesIO(image_response.content))

                        st.session_state.image = image

                    except Exception:

                        st.toast("🖼️ Image server is busy, skipping visual...")

                    st.rerun()

                except Exception as e:

                    st.error(e)

    else:

        st.write("Choices will appear here.")


if start_story:

    try:

        st.session_state.chat = client.chats.create(
            model="gemini-2.5-flash"
        )

        prompt = f"""
{SYSTEM_PROMPT}

Start a brand new {genre} visual novel.

The player has just entered the story.

Generate the opening scene.
"""

        response = st.session_state.chat.send_message(prompt)

        data = json.loads(response.text)

        st.session_state.story = data["story_text"]
        st.session_state.image_prompt = data["image_prompt"]
        st.session_state.options = data["options"]

        tts = gTTS(st.session_state.story)

        filename = f"narration_{uuid.uuid4().hex}.mp3"

        tts.save(filename)

        with open(filename, "rb") as audio:
            st.session_state.audio_file = audio.read()

        # Generate Image
        try:
            image_url = (
                f"https://image.pollinations.ai/prompt/"
                f"{st.session_state.image_prompt}"
            )

            image_response = requests.get(image_url)

            image = Image.open(BytesIO(image_response.content))

            st.session_state.image = image

        except Exception:
            st.toast("🖼️ Image server is busy, skipping visual...")

        st.rerun()

    except json.JSONDecodeError:
        st.error("Gemini returned invalid JSON.")

    except Exception as e:
        st.error(e)