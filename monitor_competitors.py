def monitor_competitors():
    competitor_profile_urls = [
        'https://www.linkedin.com/in/anuragtiwarime/',
        'https://www.linkedin.com/in/-sudhanshu-kumar/',
        'https://www.linkedin.com/in/hiteshchoudhary/',
    ]

    new_connections = []

    for profile_url in competitor_profile_urls:
        # Fetch the LinkedIn profile page
        response = requests.get(profile_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            connections_section = soup.find('section', {'id': 'connections'})

            if connections_section:
                # Extract the list of connections
                connections = connections_section.find_all('li', {'class': 'connection-item'})

                for connection in connections:
                    # Extract the connection details (name, profile URL, etc.)
                    connection_name = connection.find('span', {'class': 'actor-name'}).text
                    connection_profile_url = connection.find('a')['href']

                    # Store the connection data in a dictionary
                    connection_data = {
                        'name': connection_name,
                        'profile_url': connection_profile_url,
                    }

                    new_connections.append(connection_data)

    return new_connections
