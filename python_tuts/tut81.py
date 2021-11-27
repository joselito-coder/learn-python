import requests

# r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")

# print(r.text)

# quick exercise:

data = {
    "title":"this is good",
    "body" : "Harry bhai is the best",
    "userId" :3242
}

re = requests.post('https://jsonplaceholder.typicode.com/posts',data)

print(re.text)