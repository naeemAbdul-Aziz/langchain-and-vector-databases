import requests

google_api_key = "YOUR_GOOGLE_API_KEY"
google_cse_id = "YOUR_GOOGLE_CSE_ID"
query = "Mars rover news"

url = f"https://customsearch.googleapis.com/customsearch/v1?q={query}&cx={google_cse_id}&key={google_api_key}"
response = requests.get(url)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.json())
