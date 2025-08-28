import streamlit as st
from PIL import Image

st.title("Tralarero")

st.header("BRR BRR PATAPIN TRALARERO TRALALA")
st.write("Anuel la Doble AA ")
image = Image.open("trala.png")

st.image(image, caption="trala")

texto = st.text_input("escribe algo", "este es mi texto")
st.write("el texto escrito es",texto)

                      
