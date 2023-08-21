def generate_message(profile_data):
    message_template = "Hi {name}, I noticed that you recently connected with one of my competitors on LinkedIn. I would love to connect with you as well and learn more about your work at {company}."
    
    name = profile_data.get('name')
    company = profile_data.get('company')

    if name and company:
        message_text = message_template.format(name=name, company=company)
        return message_text

    return None
