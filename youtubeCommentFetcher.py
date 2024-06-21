import requests
import sqlalchemy as db
import pandas as pd

#default id for the video and API key
API_KEY = "AIzaSyD1AsmB66YJl8RN-YDHbWHBclTBDsjFkDY"
default_id = "X8VuIq4j1bo"

#function to get the key word to search
def get_key_word():
    while True: #loop until a valid response is given
        search_on_word = input("Would you like to filter based on any key word(s)? type 'y' for yes or 'n' for no: ")
        #if the user wants to search by a key word get the word
        if (search_on_word == 'y'): 
            key_word = input("Enter the desired key word to search for: ")
            return key_word
        #if the user does not want to search by a key word return none
        elif search_on_word == 'n':
            return None
        #else keep running the loop until a valid response is given
        else:
            print("Invalid response. Enter either 'y' or 'n'.")

#function to get the sorting method
def get_sorting_method():
    while True: #loop until a valid response is given
        sorted_order = input("Enter 't' to filter by the most recent comments or 'r' to filter by relevance: ")
        #if sorted input is t sort by time
        if sorted_order == 't': 
            return "time"
        #if sorted input is r sort by relevance
        elif sorted_order == "r":
            return "relevance"
        #else keep running the loop until a valid response is given
        else:
            print("Invalid sorting method. Enter 't' or 'r'.")

#get a video URL from the user to extract the id
video_id = ""
video_url = input("Enter a Youtube video URL, type 'd' to use the default video: ")

#if the user inputs 'd', use the default video
if video_url == 'd':
    video_id = default_id
else:  #else extract the id from the user's URL
    video_id = video_url[32:]

#prompt the user for a key word
key_word = get_key_word()

#get sorting method
filter = get_sorting_method()


#construct the API request URL based on user inputs
if key_word:
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={API_KEY}&maxResults=20&order={filter}&searchTerms={key_word}"
else:
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={API_KEY}&maxResults=20&order={filter}"

#send GET request to API
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
