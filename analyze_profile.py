def analyze_profile(profile_url):
    profile_data = {}

    # Fetch the LinkedIn profile page
    response = requests.get(profile_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the 'About' section
        about_section = soup.find('section', {'class': 'summary'})
        if about_section:
            about_text = about_section.find('p').text.strip()
            profile_data['about'] = about_text

        # Extract the job title and company name
        experience_section = soup.find('section', {'id': 'experience-section'})
        if experience_section:
            job_title_element = experience_section.find('h3', {'class': 't-16 t-black t-bold'})
            company_element = experience_section.find('p', {'class': 'pv-entity__secondary-title t-14 t-black t-normal'})

            if job_title_element:
                job_title_text = job_title_element.text.strip()
                profile_data['job_title'] = job_title_text

            if company_element:
                company_text = company_element.text.strip()
                profile_data['company'] = company_text

    return profile_data
