import requests

def shorten_link(full_link):
    api_key = 'a87507135b3ae623a2b86ffefbbe1568dc9cb'
    base_url = 'https://cutt.ly/api/api.php'


    payload = {'key': api_key, 'short': full_link}

    try:

        response = requests.get(base_url, params=payload)
        data = response.json()

        if data['url']['status'] == 7:
            short_link = data['url']['shortLink']
            print('Shortened Link:', short_link)
        else:

            status_code = data['url']['status']
            status_description = {
                1: 'The shortened link comes from the domain that shortens the link.',
                2: 'The entered link is not a valid link.',
                3: 'The preferred link name is already taken.',
                4: 'Invalid API key.',
                5: 'The link has not passed the validation. Includes invalid characters.',
                6: 'The link provided is from a blocked domain.',
                8: 'You have reached your monthly link limit. You can upgrade your subscription plan to add more links.'
            }
            print('Error:', status_description.get(status_code, 'Unknown status'))

    except requests.exceptions.RequestException as e:

        print("Request Error:", e)
    except KeyError:

        print("Error: Invalid response from the API")

if __name__ == "__main__":
    link = input("Enter a link: ")
    shorten_link(link)
