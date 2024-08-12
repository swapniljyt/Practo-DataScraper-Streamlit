from src.url_generator import generator
from src.scrapper import doctor_scrapper
import streamlit as st
import pandas as pd


st.title('Practo-Doctor-Datascrapper')

st.header('Enter the input features:')
location = st.text_input("Doctor Location:")
specialization = st.text_input("Doctor Specialization:")
pages=10
progress_bar = st.progress(0)
status_text = st.empty()
if st.button('Scrap'):
    all_doctors=[]
    for page in range(pages+1):
        url=generator(location,specialization,page)
        data=doctor_scrapper(url)
        progress = int((page / pages) * 100)
        progress_bar.progress(progress)
        status_text.text(f"Scraping page {page}...")
        if data:
            all_doctors.extend(data)
        else:
            st.write("no doctor Found on this page")
            break
    progress_bar.empty()
    status_text.text("Scraping complete!")        
    st.write(pd.DataFrame(all_doctors))            


