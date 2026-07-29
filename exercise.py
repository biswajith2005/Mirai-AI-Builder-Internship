import streamlit as st
import requests
import urllib.parse


st.title("The AI Image Studio")

st.sidebar.header("Settings")
art_style=st.sidebar.selectbox("Select a Style",[
    "Photorealistic",
    "Cinematic",
    "Anime",
    "Studio Ghibli",
    "3D Render",
    "Digital Art",
    "Fantasy Art",
    "Cyberpunk",
    "Oil Painting",
    "Watercolor",
    "Pencil Sketch",
    "Pixel Art",
    "Minimalist",
    "Comic Book",
    "Neon",
    "Vintage",
    "Surreal",
    "Isometric 3D",
    "Clay Art",
    "Origami"
])

image_width = st.sidebar.number_input(
    "Width",
    min_value=64,
    max_value=2048,
    value=1024
)

image_height = st.sidebar.number_input(
    "Height",
    min_value=64,
    max_value=2048,
    value=1024
)

image_width=st.sidebar.slider("WIDTH",min_value=64,max_value=2048,value=1024)
image_height=st.sidebar.slider("HEIGHT",min_value=64,max_value=2048,value=1024)


use_message=st.text_input("Describe your thoughts..")
#Add button
if st.button("Generate Image"):
    if use_message:
        with st.spinner("Cooking the image"):
            full_prompt = f"""
{use_message},
Art style: {art_style},
masterpiece, best quality, ultra-detailed, 8K, cinematic composition,
professional lighting, volumetric lighting, dramatic shadows,
sharp focus, highly realistic textures, vibrant colors,
photorealistic, HDR, depth of field, award-winning digital art,
intricate details, visually stunning, clean background,
perfect anatomy, high contrast, epic atmosphere
"""
            prompt = urllib.parse.quote(full_prompt)

            url = (f"https://image.pollinations.ai/prompt/{prompt}"f"?width={image_width}&height={image_height}")
            response=requests.get(url )

            if response.status_code==200:
                st.success("Image Generated")
                st.image(response.content,caption=full_prompt)
                st.download_button(
                    label="Download Image",
                    data=response.content,
                    file_name="my_image.png",
                    mime="image/* "
                )
            else:
                st.error("API not working")
    else:
        st.warning("Please add an image description")