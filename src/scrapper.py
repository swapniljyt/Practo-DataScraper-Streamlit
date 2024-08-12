import requests
from bs4 import BeautifulSoup
def doctor_scrapper(url):
    headers = {"User-Agent": "Your User Agent"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    doctor_data = []

    no_response_message=soup.find("span", {"data-qa-id": "no_results_description"})
    if no_response_message:
        print(no_response_message.text.strip())
        return []

    else:
        doctors = soup.find_all("div", class_="info-section")
        for doctor in doctors:
            name= doctor.find("h2", class_="doctor-name")
            if name:
                name = name.text.strip()
            else:
                continue    
                
            specialization = doctor.find("div", class_="u-grey_3-text").find("span")
            specialization = specialization.text.strip() if specialization else "N/A"
    
            
            experience = doctor.find("div", {"data-qa-id": "doctor_experience"})
            experience = experience.text.strip() if experience else "N/A"
    
            
            locality_tag = doctor.find("span", {"data-qa-id": "practice_locality"})
            locality = locality_tag.text.strip() if locality_tag else "N/A"


            doctor_data.append({
                "Doctor": name,
                "Specialization": specialization,
                "Experience": experience,
                "Practice Locality": locality
            })
        return doctor_data






    