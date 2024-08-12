from src.url_generator import generator
from src.scrapper import doctor_scrapper
url=generator("Bengaluru","Cardiologist","1")
print(url)

data=doctor_scrapper(url)

if data:
    print(data)

else:
    print("No doctor found at this location")

