# app.py
import streamlit as st
from transformers import pipeline

# Load image-to-text pipeline
@st.cache_resource
def load_image_to_text_model():
    return pipeline("image-to-text")

image_to_text_model = load_image_to_text_model()

# Streamlit UI
st.title("Image to Text Converter")
st.markdown("By Ahmed Fayad")

uploaded_image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    if st.button("Generate Caption"):
        caption = image_to_text_model(uploaded_image)
        st.success(f"Caption: {caption[0]['generated_text']}")