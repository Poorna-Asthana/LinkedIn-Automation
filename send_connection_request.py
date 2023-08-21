def send_connection_request(linkedin_client, profile_url):
    try:
        # Fetch the LinkedIn profile ID from the URL
        profile_id_start_index = profile_url.rfind('/') + 1
        profile_id_end_index = profile_url.rfind('?')
        if profile_id_end_index == -1:
            profile_id_end_index = len(profile_url)

        profile_id = profile_url[profile_id_start_index:profile_id_end_index]

        # Send the connection request with a personalized message
        message_text = generate_message(analyze_profile(profile_url))
        
        if message_text:
            linkedin_client.send_invitation(
                invitation_message=message_text,
                profile_id=profile_id,
            )

            print(f"Connection request sent to {profile_url}")
        
    except ChallengeException as e:
        print(f"Failed to send connection request to {profile_url}: {e}")
