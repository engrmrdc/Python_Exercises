# Create a function named check_website that checks if a website is up or down.

# The function should take one parameter:

# url (a string) - the URL of the website to check.
# The function should return a string: "Website is Up" or "Website is Down".

import requests
def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Website is Up"
        else:
            return "Website is Down"
    except requests.ConnectionError:
        return "Website is Down"

# Under this line are the data for testing.
url = 'https://www.netflix.com'
check_website(url)
