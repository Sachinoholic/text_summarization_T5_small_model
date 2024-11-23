import requests

# URL of the deployed API
# url = "http://localhost:8000/summarize"  # FastAPI
url = "http://localhost:5000/summarize"  # Flask

# Test input
data = {
    "text": "Machine learning is a method of data analysis that automates analytical model building."
}

# Send POST request
response = requests.post(url, json=data)

# Print the response
if response.status_code == 200:
    print("Summary:", response.json()["summary"])
else:
    print("Error:", response.json())
