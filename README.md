# YouTube Comments Fetcher
This project fetches comments from a specified YouTube video using the YouTube Data API, filters them based on user input, and stores the comments in an SQLite database.

### Table of Contents
- [Setup Instructions](#set-up-instructions)
- [How to Run the Code](#how-to-run-the-code)
- [Overview of the Code](#overview-of-the-code)

### Set Up Instructions
#### Prerequisites:
Before you begin, ensure you have the following installed:
* Python 3.6+
* requests library
* sqlalchemy library
* pandas library
* To install:
    * ```python
      pip install requests sqlalchemy pandas
      ```


#### Setting Up The Repository:
1. **Clone the repository**
    * ```python
      git clone https://github.com/ETAMARKIN17/youtube-comments-fetcher.git
      cd youtube-comments-fetcher
      ```
2. **Set up environment variables**
    * Obtain an API key from the Google Developer website for the YouTube Data API.
    * Set the API_KEY variable in your code with this obtained key.
### How To Run The Code
1. **Run the script**
    * ```python
      python3 youtubeCommentFetcher.py
      ```
2. **Follow the prompts**
    * Paste a YouTube video URL or type 'd' to use the default video.
      * The default video is *"The Most Violent and Brutal Knockouts in UFC History"*
      * Default id: X8VuIq4j1bo
    * Choose whether to filter comments based on a keyword.
    * Select the sorting method (by time('t') or relevance('r')).  


3. **Check the output**
    * The script will display the status of the request and print the fetched comments if successful.
    * The comments will be saved in an SQLite database (youtubeComments.db).

### Overview Of The Code
1. #### Imports:
    * **requests:** To make HTTP requests to the YouTube Data API.
    * **sqlalchemy:** To interact with the SQLite database.
    * **pandas:** To handle data manipulation and storage.  


2. #### Constants:
    * **API_KEY:** Your YouTube Data API key.
    * **default_id:** Default YouTube video ID.  


3. #### Functions:
    * **get_key_word():** Prompts the user to enter a keyword for filtering comments.
    * **get_sorting_method():** Prompts the user to choose a sorting method (time or relevance).  

  
4. #### Main Logic:
    * Prompts the user for a YouTube video URL.
    * Constructs the API request URL based on user inputs.
    * Sends a GET request to the YouTube Data API.
    * Extracts relevant data from the API response.
    * Stores the data in an SQLite database using pandas and sqlalchemy.
    * Prints the fetched comments and verifies the stored data.  


5. #### Error Handling:
    * Checks the status of the API request.
    * Prints an error message if the request fails.




