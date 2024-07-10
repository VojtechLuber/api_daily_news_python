import requests

api_key = "18b8baff3ebc4e7a91fd3ab62c435818"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-06-10&sortBy=publishedAt&apiKey=" \
      "18b8baff3ebc4e7a91fd3ab62c435818"


# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
for article in content ["articles"]:
    print(article["title"])