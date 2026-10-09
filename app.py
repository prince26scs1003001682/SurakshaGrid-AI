# app.py
# Stage 2: Image upload and preview
# We will keep this simple and test it before adding AI analysis.

import streamlit as st
from PIL import Image

st.title("SurakshaGrid AI")
st.write("Disaster Evidence Mapper")
st.caption("Upload an image to check if it contains flooding or road damage.")

# Image uploader
uploaded_file = st.file_uploader(
    "Upload a disaster image",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:
    # Open the uploaded file as an image
    image = Image.open(uploaded_file)

    # Show the image in the app
    st.image(image, caption="Uploaded image", use_container_width=True)

    # Show image information
    st.write(f"Image name: {uploaded_file.name}")
    st.write(f"Image size: {image.size}")

    # Simple status message
    st.success("Image uploaded successfully. Ready for the next analysis stage.")
else:
    st.info("No image uploaded yet. Please upload a disaster image to continue.")
