import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from services.text_service import generate_text
from services.image_service import generate_image
from PIL import Image
import io

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="AI Content Pipeline",
    page_icon="🚀",
    layout="wide"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #1c1f26;
        color: white;
    }
    .stTextArea textarea {
        background-color: #1c1f26;
        color: white;
    }
    .stButton button {
        background: linear-gradient(90deg, #ff4b2b, #ff416c);
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.title("🚀 AI-Powered Creative Content Generator")
st.markdown("Generate **text ✍️** and **images 🎨** using AI")

# -------------------- TABS --------------------
tab1, tab2 = st.tabs(["📝 Text Generation", "🎨 Image Generation"])

# ==================== TEXT TAB ====================
with tab1:
    st.subheader("Generate Text")

    prompt = st.text_area("Enter your prompt", height=150)

    if st.button("Generate Text"):
        if prompt.strip() == "":
            st.warning("Please enter a prompt.")
        else:
            with st.spinner("Generating text..."):
                result = generate_text(prompt)

            st.success("Done!")
            st.write(result)

# ==================== IMAGE TAB ====================
with tab2:
    st.subheader("Generate Image")

    col1, col2 = st.columns(2)

    with col1:
        img_prompt = st.text_area("Enter image prompt", height=150)

        generate_btn = st.button("Generate Image")

    with col2:
        if generate_btn:
            if img_prompt.strip() == "":
                st.warning("Please enter a prompt.")
            else:
                with st.spinner("Generating image..."):
                    image_bytes = generate_image(img_prompt)

                if image_bytes:
                    image = Image.open(io.BytesIO(image_bytes))
                    st.image(image, caption="Generated Image", use_column_width=True)

                    # Download button
                    buf = io.BytesIO()
                    image.save(buf, format="PNG")

                    st.download_button(
                        label="Download Image",
                        data=buf.getvalue(),
                        file_name="generated.png",
                        mime="image/png"
                    )
                else:
                    st.error("Image generation is slow or busy. Please try again in a few seconds.")



import time

# inside image button logic
time.sleep(2)