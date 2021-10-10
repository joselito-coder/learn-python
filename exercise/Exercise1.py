# Question ==> Create a dictionary and take input from the user and return the meaning of the word from the dictionary

# Solution:
word_dict = {
    "anime":"Anime is hand-drawn and computer animation originating from Japan.\nWiki reference: https://en.wikipedia.org/wiki/Anime",
    "cryptography":"Cryptography, or cryptology, is the practice and study of techniques for secure communication in the presence of adversarial behavior\nWiki reference: https://en.wikipedia.org/wiki/Cryptography",
    "data processing": "Data processing is, generally, \"the collection and manipulation of items of data to produce meaningful information.\"\nWiki reference: https://en.wikipedia.org/wiki/Data_processing",
    "data structure": "In computer science, a data structure is a data organization, management, and storage format that enables efficient access and modification\nWiki reference: https://en.wikipedia.org/wiki/Data_structure"
}

print("Enter your word: ")
word = input()

print("\n"+word_dict.get(word))