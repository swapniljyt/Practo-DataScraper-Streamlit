from src.url_generator import generator
from src.scrapper import doctor_scrapper
import streamlit as st
import pandas as pd


st.title('Practo-Doctor-Datascrapper')

st.header('Enter the input features:')
location = st.text_input("Doctor Location:")
specialization = st.text_input("Doctor Specialization:")
pages=10

if st.button('Scrap'):
    all_doctors=[]
    for page in range(pages+1):
        url=generator(location,specialization,page)
        data=doctor_scrapper(url)
        if data:
            st.write(f"Scraping page{page}...")
            all_doctors.extend(data)
        else:
            st.write("no doctor Found on this page")
            break
    st.write(pd.DataFrame(all_doctors))            



    url=generator(location,specialization,"1")
    data=doctor_scrapper(url)
    if data:
    print(data)
    else:
    print("No doctor found at this location")