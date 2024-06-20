import requests
import sqlalchemy as db
import pandas as pd

#default id for the video and API key
API_KEY = "AIzaSyD1AsmB66YJl8RN-YDHbWHBclTBDsjFkDY"
default_id = "X8VuIq4j1bo"

#get a video URL from the user to extract the id
video_id = ""
video_url = input("Enter a video URL, type 'd' to use the default video: ")

#if the user inputs 'd', use the default video
if video_url == 'd':
    video_id = default_id
else:  #else extract the id from the user's URL
    video_id = video_url[32:]

#use the id and API key to set a GET request for the comments
url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={API_KEY}&maxResults=20"
response = requests.get(url)

#print the status of the request
print("STATUS: ", response.status_code)
data = response.json()

#check if the request was successful
if response.status_code == 200:
    #initialize lists to store the data I want to keep
    comments = []
    authors = []
    published = []
    likes = []
    replies = []

    #extract data from the JSON response
    for item in data.get('items', []):
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        published_date = item['snippet']['topLevelComment']['snippet']['publishedAt']
        like_count = item['snippet']['topLevelComment']['snippet']['likeCount']
        reply_count = item['snippet']['totalReplyCount']

        #append all of the data to the lists
        comments.append(comment)
        authors.append(author)
        published.append(published_date)
        likes.append(like_count)
        replies.append(reply_count)


    #create a new dictionary with the extracted data
    extracted_data = {
        'comment': comments,
        'author': authors,
        'date_published': published,
        'likes': likes,
        'replies': replies
    }

    #convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(extracted_data)

    #save the DataFrame to an SQLite database
    engine = db.create_engine('sqlite:///youtubeComments.db')
    df.to_sql('comments', con=engine, if_exists='replace', index=False)

    #query the database to verify the data
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM comments;")).fetchall()
        print(pd.DataFrame(query_result))
else:
    #if the request failed, print an error message
    print("Failed to fetch comments")
    print(data)
