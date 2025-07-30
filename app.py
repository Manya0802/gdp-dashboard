import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.set_page_config(layout="centered")
st.title("🎨 Lehenga Color Changer")

uploaded = st.file_uploader("Upload lehenga image", type=["png", "jpg", "jpeg"])

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    image_np = np.array(image)

    st.image(image_np, caption="Original", use_column_width=True)

    # Dummy color selection and dummy mask (rectangular)
    hex_color = st.color_picker("Choose lehenga color", "#ff69b4")
    new_color = tuple(int(hex_color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))

    h, w, _ = image_np.shape
    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.rectangle(mask, (w//3, h//3), (2*w//3, 5*h//6), 255, -1)

    recolored = image_np.copy()
    for c in range(3):
        recolored[:, :, c] = np.where(mask == 255, new_color[c], recolored[:, :, c])

    st.image(recolored, caption="Recolored Lehenga", use_column_width=True)
