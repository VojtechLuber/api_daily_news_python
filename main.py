import requests
from  send_email import send_email

api_key = "18b8baff3ebc4e7a91fd3ab62c435818"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-06-10&sortBy=publishedAt&apiKey=" \
      "18b8baff3ebc4e7a91fd3ab62c435818"


# make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
body = ""
for article in content ["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
