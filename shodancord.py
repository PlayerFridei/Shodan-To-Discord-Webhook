import requests
import shodan
import time
import argparse
import random
import string

# Epic tool created by PlayerFridei
# Shodancord version 0.1 Early Testing

# Shodan API key
SHODAN_API_KEY = 'API KEY HERE'

# Discord webhook URL
DISCORD_WEBHOOK_URL = 'DISCORD WEBHOOK HERE'

# Specific query
SPECIFIC_QUERY = 'SHODAN QUERY HERE'

# Number of pages to fetch
NUM_PAGES = 1  # Change this to the desired number of pages

# Initialize Shodan API
api = shodan.Shodan(SHODAN_API_KEY)

# Function to send data to Discord webhook
def send_to_discord(ip, country, server_info, image_url):
    try:
        # Ensure that all required fields are non-empty strings
        ip = ip if ip else "N/A"
        country = country if country else "Unknown"
        server_info = server_info if server_info else "No additional data available"
        image_url = image_url if image_url else 'https://via.placeholder.com/150'  # Placeholder image if none available

        payload = {
            "username": "Shodan Webhook",
            "embeds": [
                {
                    "title": "Shodancord Webhook",
                    "description": f"**IP:** {ip}\n**Country:** {country}\n**Server Info:** {server_info}",
                    "url": f"http://{ip}",
                    "image": {"url": image_url},
                    "color": 15258703  # Light blue color
                }
            ]
        }

        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 200 or 204:
            print("Message sent successfully to Discord webhook")
        else:
            print(f"Failed to send message to Discord webhook. Status code: {response.status_code}")
            print(response.text)  # Print response content for debugging
    except Exception as e:
        print(f"Error sending message to Discord webhook: {e}")

# Function to fetch and send Shodan data
def fetch_and_send(query, num_pages, rate_limit):
    try:
        # Perform Shodan search
        for page in range(1, num_pages + 1):
            print(f"Fetching page {page} of results...")
            results = api.search(query, page=page)

            # Check if there are any results
            if results['total'] > 0:
                for result in results['matches']:
                    ip = result.get('ip_str', "N/A")
                    country = result.get('location', {}).get('country_name', 'Unknown')
                    server_info = result.get('data', 'No additional data available')

                    # Attempt to get the screenshot URL if available
                    image_url = result.get('opts', {}).get('screenshot', {}).get('data', 'https://via.placeholder.com/150')

                    # Send payload to Discord webhook
                    send_to_discord(ip, country, server_info, image_url)
                    print(f"Message sent for IP: {ip}")
                    time.sleep(rate_limit)  # Delay to avoid spamming the webhook
            else:
                print("No results found.")
                break
    except shodan.APIError as e:
        print(f"Shodan API error: {e}")
    except Exception as e:
        print(f"Error fetching and sending data: {e}")

# Function to test the Discord webhook with random data
def test_webhook():
    try:
        random_ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))
        random_country = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        random_server_info = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        random_image_url = 'https://via.placeholder.com/150'  # Placeholder URL for testing

        send_to_discord(random_ip, random_country, random_server_info, random_image_url)
        print("Webhook test successful.")
    except Exception as e:
        print(f"Error testing webhook: {e}")

# Main function to parse command line arguments
def main():
    parser = argparse.ArgumentParser(description='Script to fetch and send Shodan data to Discord webhook')
    parser.add_argument('--debugtest', action='store_true', help='Test the Discord webhook with random data')
    parser.add_argument('--sleep', type=int, default=24, help='Sleep time in hours between data fetch cycles')
    parser.add_argument('--rate-limit', type=float, default=1.0, help='Rate limit in seconds between sending each message to the Discord webhook')
    args = parser.parse_args()

    if args.debugtest:
        test_webhook()
    else:
        sleep_time = args.sleep * 3600  # Convert hours to seconds
        rate_limit = args.rate_limit
        while True:
            print("Starting new data fetch cycle...")
            fetch_and_send(SPECIFIC_QUERY, NUM_PAGES, rate_limit)
            print(f"Waiting for {args.sleep} hours before next fetch...")
            # Wait for the specified number of hours
            time.sleep(sleep_time)

if __name__ == "__main__":
    main()
