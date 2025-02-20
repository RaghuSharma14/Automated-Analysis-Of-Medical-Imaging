import os
os.system('pip install cython')


import streamlit as st
import cv2
import numpy as np
from PIL import Image
from detect import blood_cell_count


st.title("Blood Cell Counting App")

uploaded_file = st.file_uploader("Upload an image of a blood smear...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Process the image using blood_cell_count
    output_image, rbc_count, wbc_count, platelet_count = blood_cell_count(image)

    # Display counts
    st.write(f"Total RBC: {rbc_count}")
    st.write(f"Total WBC: {wbc_count}")
    st.write(f"Total Platelets: {platelet_count}")

    # Convert image to RGB format for Streamlit display
    output_image_rgb = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)
    st.image(output_image_rgb, caption="Processed Image", use_container_width=True)

