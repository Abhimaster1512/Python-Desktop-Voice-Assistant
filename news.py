import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")


def get_news():

    url = (
        f"https://newsapi.org/v2/top-headlines"
        f"?country=us&apiKey={API_KEY}"
    )

    try:
        response = requests.get(url)
        data = response.json()

        articles = data["articles"][:5]

        headlines = []

        for article in articles:
            headlines.append(article["title"])

        return "Here are the latest news headlines. " + ". ".join(headlines)

    except:
        return "Unable to fetch news."