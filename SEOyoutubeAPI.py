import requests

#defult id for the video and my API key
API_KEY = "AIzaSyD1AsmB66YJl8RN-YDHbWHBclTBDsjFkDY"
default_id = "X8VuIq4j1bo"

#get a video url from the user to extract the id
video_id = ""
video_url = input("Enter a video url, type 'd' to use the default video: ")

#if the user inputs 'd' use the defult video
if (video_url == 'd'):
  video_id = default_id
else: #else extract the id from the users url
  video_id = video_url[32:]

#use the id and API key to set a get request for the comments
url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={API_KEY}&maxResults=20"
response = requests.get(url)

#print the status of the request
print("STATUS: ", response.status_code)
data = response.json()

#if it goes through print the top 20 comments with the author name
if response.status_code == 200:
    for item in data.get('items', []):
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        print(f"Author: {author}, Comment: {comment}")
else: #if it doesnt print failed
    print("Failed to fetch comments")
    print(response.json())
