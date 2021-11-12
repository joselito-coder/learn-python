# Problem Statement:-
# You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. The most relevant sentence is the one with the maximum number of matching words with the query.
# Sentences = ["Python is cool", "python is good", "python is not python snake"]
# Input:
# Please input your query string
# "Python is"
# Output:
# 3 results found:
#     python is not python snake
#     python is good
#     Python is cool

"""
Author: Joselito
Date: 12-11-2021
Purpose: To Create a search engine using python
"""

# Practice Problem 7 solution:

def searchWord(sentences,query_string):
    # Dictionary for storing the relevance of each sentence
    relevance = { sentence:0 for sentence in sentences }

    # Loop through the sentences and 
    for sentence in sentences:
        # check if the query string is in that sentence
        if query_string in sentence:
            # loop through the sentence and 
            # Check for the occurance of that query_string in that sentence
            # increment every time the word is found
            for word in sentence.split():
                if query_string in word:
                    relevance[sentence] += 1
        # If the query is not found in sentence then remove it from the relevance dict
        else:
            relevance.pop(sentence)

    # If there are search results display them
    if len(relevance) != 0:
        # sort Relevance of the sentence based on the relevance count
        sorted_relevance = sorted(relevance.items(),key=lambda kv:kv[1],reverse=True)

        print(f"\n{len(sorted_relevance)} results found:")

        # Print all the search results found
        for key,value in  sorted_relevance :
            print(f"\t{key}")
    else:
        print("No Search Result found")


if __name__ == "__main__":
    sentences = ["Python is cool","python is good", "python is not python snake"]

    # take user input
    query = input("Enter Your query: ")

    # search the word
    searchWord(sentences, query)