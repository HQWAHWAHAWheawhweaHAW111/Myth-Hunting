import streamlit as st
from modules.screen_capture import capture_screen
from modules.ocr_processing import extract_text
from modules.ai_assistant import ask_ai

st.title("AI Screen Assistant")

if st.button("Capture Screen"):
    image_path = capture_screen()
    text = extract_text(image_path)
    st.image(image_path, caption="Captured Screen")
    st.write("Extracted Text:", text)
    
    response = ask_ai(text)
    st.write("AI Response:", response)
