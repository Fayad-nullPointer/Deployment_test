# app.py
import streamlit as st
from transformers import pipeline
from PIL import Image

# Load image-to-text pipeline
@st.cache_resource
def load_image_to_text_model():
    return pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

image_to_text_model = load_image_to_text_model()

# Streamlit UI
st.title("🖼️ Image to Text Converter")
st.markdown("By **Ahmed Fayad**")

uploaded_image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    try:
        image = Image.open(uploaded_image).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Generate Caption"):
            with st.spinner("Generating caption..."):
                caption = image_to_text_model(image)
                st.success(f"**Caption:** {caption[0]['generated_text']}")
    except Exception as e:
        st.error(f"Error processing image: {e}")
