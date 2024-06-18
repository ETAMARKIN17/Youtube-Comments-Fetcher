import requests

API_KEY = "AIzaSyD1AsmB66YJl8RN-YDHbWHBclTBDsjFkDY"
channel_id = "UC4wk6LOaMK7_hqrj2-Xu8gQ"

url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={API_KEY}"
response = requests.get(url)

print("STATUS: ", response.status_code)
print(response.json())



