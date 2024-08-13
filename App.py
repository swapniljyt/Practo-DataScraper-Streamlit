from src.url_generator import generator
from src.scrapper import doctor_scrapper
import streamlit as st
import pandas as pd


st.title('Practo-Doctors-Datascrapper👨‍⚕️')

st.header('Enter the required informtion:')
location = st.text_input("Doctor Location City:")
specializations = [
    "Surgeon","Ophthalmologist", "Dermatologist", "Cardiologist", "Psychiatrist",
    "Gastroenterologist", "ear-nose-throat (ent) specialist", "Gynecologist / Obstetrician",
    "Neurologist", "Urologist", "Dentist", "Prosthodontist", "Orthodontist",
    "Pediatric Dentist", "Endodontist", "Implantologist", "Ayurveda",
    "Homoeopath", "Siddha", "Unani", "Yoga & Naturopathy", "Acupuncturist",
    "Physiotherapist", "Psychologist", "Audiologist", "Speech Therapist",
    "Dietitian/Nutritionist"
]
specialization = st.selectbox("Select a specialization:", specializations)
pages=10
count=0
progress_bar = st.progress(0)
status_text = st.empty()
if st.button('Scrap'):
    all_doctors=[]
    for page in range(pages+1):
        url=generator(location,specialization,page)
        data=doctor_scrapper(url)
        progress = int((page / pages) * 100)
        progress_bar.progress(progress)
        status_text.text(f"Scraping page😊 {page}...")
        if data:
            all_doctors.extend(data)
            count+=1
        else:
            break
    if(count>0):
        import streamlit as st
        st.markdown(f'<small>There are {len((pd.DataFrame(all_doctors)))} available doctors in {location}⤵</small>', unsafe_allow_html=True)
        st.write(pd.DataFrame(all_doctors))
        status_text.text("Scraping complete✔")
        count=0
    else:
        st.markdown('**No Doctor Found ☹**')
        st.markdown('<small>Please check the input variables ⚠</small>', unsafe_allow_html=True)
        status_text.text("Scraping complete✔")  

    progress_bar.empty()           


