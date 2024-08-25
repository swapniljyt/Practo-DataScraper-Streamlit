from src.url_generator import generator
from src.scrapper import doctor_scrapper
import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    body {
        background-color: #BBE6F8;  /* Milky modern sky blue */
    }
    .reportview-container .main {
        background-color: #e0f7fa;  /* Milky modern sky blue */
        padding: 10px;
    }
    .stButton button {
        background-color: #E590C6;
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 12px;
        border: 2px solid #EB189E;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #F683CC;
        color: white;
    }
    .stTextInput > div > input {
        border: 2px solid #008CBA;
        border-radius: 10px;
    }
    .stSelectbox > div > div {
        border: 2px solid #008CBA;
        border-radius: 10px;
    }
    .stDownloadButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 12px;
        border: 2px solid #4CAF50;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stDownloadButton button:hover {
        background-color: #388E3C;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)


st.title('Practo Doctors Data Scraper 👨‍⚕️')
st.markdown("<h2 style='text-align: center; color: #008CBA;'>Find the Best Doctors Near You</h2>", unsafe_allow_html=True)


with st.container():
    st.header('Enter the required information:')
    col1, col2 = st.columns(2)
    
    with col1:
        location = st.text_input("Doctor Location City:")
    
    with col2:
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

# Scraping process
pages = 10
count = 0
progress_bar = st.progress(0)
status_text = st.empty()

if st.button('Scrap Data'):
    all_doctors = []
    for page in range(pages + 1):
        url = generator(location, specialization, page)
        data = doctor_scrapper(url)
        progress = int((page / pages) * 100)
        progress_bar.progress(progress)
        status_text.text(f"Scraping page {page}... ⌛")
        
        if data:
            all_doctors.extend(data)
            count += 1
        else:
            break

    if count > 0:
        df = pd.DataFrame(all_doctors)
        st.markdown(f'<small>Found **{len(df)}** doctors in **{location}**.</small>', unsafe_allow_html=True)
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Data as CSV 📥",
            data=csv,
            file_name=f'doctors_in_{location}.csv',
            mime='text/csv',
        )
        status_text.text("Scraping complete ✔")
    else:
        st.markdown('<small><strong>No doctors found. Please check your input variables.🙁</strong></small>', unsafe_allow_html=True)
        status_text.text("Scraping complete ✔")
        
    progress_bar.empty()

