from src.url_generator import generator
from src.scrapper import doctor_scrapper
import streamlit as st


st.title('Practo-Doctor-Datascrapper')

st.header('Enter the input features:')
location = st.text_input("Doctor Location:")
specialization = st.text_input("Doctor Specialization:")

if st.button('Scrap'):
    url=generator(location,specialization,"1")
    data=doctor_scrapper(url)
    if data:
    print(data)
    else:
    print("No doctor found at this location")