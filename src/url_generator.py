def generator(location,specialization,page_no):
    forma_location=location.lower().replace(' ', '-')
    forma_specialization=specialization.lower().replace(' ', '-')

    url = f"https://www.practo.com/{forma_location}/{forma_specialization}?page={page_no}"

    return url