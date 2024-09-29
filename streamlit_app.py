import streamlit as st 
import os 
from PIL import Image
import google.generativeai as genai 

genai.configure(api_key="AIzaSyAOxbhpdboA7sRDASmKEE0hOHNr3nLo1vw")

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_text, image_data, prompt) :
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text 

def input_image_details(uploaded_file) :
    if uploaded_file is not None :
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type" : uploaded_file.type,
                "data" : bytes_data
            }
        ]
        return image_parts
    else :
        raise FileNotFoundError("No file was uploaded")
    
st.set_page_config(page_title = "Invoice Reader")
st.sidebar.header("Bill Reader")
st.sidebar.write("Made by Abhi")
st.sidebar.write("Powered by Google Gemini AI")
st.header("Bill Reader")
st.subheader("Made by Abhi")
st.subheader("Manage your expenses")
input = st.text_input("What do you want me to do?", key="input")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
image = ""
if uploaded_file is not None :
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Submit")

input_prompt = """
You are now an expert in reading invoices. We are going to upload an image of an invoice and you will have to answer any questions
based on that invoice that the user asks you.
Make sure to greet the user first in at least three different languages preferably Japanese, Hindi and Italian
Do keep the fonts uniform and give the items list in a bullet-list format 
At the end make sure to thank the user for using our app "Bill Reader" and ask them to use it again in the future as well.
"""

if submit :
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.write(response)
