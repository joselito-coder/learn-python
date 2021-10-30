# Exercise 9 solution
# As pywin32 module is not available for linux I used pyttsx3 module for text to speech
import pyttsx3
import requests
import time
# This library is used to convert the numbers like 1 to 1st and 2 to 2nd and so on
from num2words import num2words

# Insert your api key here
api_key = '917881f413a345568743a6c335d2734b'

def getLatestNews():
    # make a request for the top headlines
    res = requests.get(f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}')

    # Convert the news to json
    news_json = res.json()

    # get the first 10 articles using slicing
    articles = news_json['articles'][:10]

    # Return the list of articles
    return articles

# This function converts the numbers like 1 to it's ordinal equivalent
def ordinal(num):
    return num2words(num,to='ordinal_num')

# This function reads out articles
def readArticles(articles):
    #  Read out each article in articles
    for count,article in enumerate(articles):
        speak(f"The {ordinal(count+1)} article is  ")
        speak(article['title'])
        speak(article['description'])
        time.sleep(2)

# Function used for speaking text
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 135)
    engine.say(text)
    engine.runAndWait()

# Main method
if __name__ == "__main__":
    articles = getLatestNews()
    readArticles(articles)