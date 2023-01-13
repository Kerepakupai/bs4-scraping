from bs4 import BeautifulSoup
# import lxml
import requests


def get_hacker_news():
    response = requests.get("https://news.ycombinator.com/news")
    yc_content = response.text

    soup = BeautifulSoup(yc_content, "html.parser")

    articles = [(article.a["href"], article.getText()) for article in soup.find_all("span", class_="titleline")]
    scores = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

    max_index = scores.index(max(scores))

    title = articles[max_index][1]
    link = articles[max_index][0]
    score = scores[max_index]

    message = f"{title} | {link} | {score} points"
    return message


def get_movies():
    response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
    html_doc = response.text

    soup = BeautifulSoup(html_doc, "html.parser")

    movies = [movie.getText() for movie in soup.find_all("h3", class_="title")]
    # movies_sorted = list(reversed(movies))
    movies_sorted = movies[::-1]

    with open("movies.txt", "w", encoding="utf-8") as file:
        file.write('\n'.join(movies_sorted))


get_movies()
