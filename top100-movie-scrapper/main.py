import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
movie_page = response.text
# print(movie_page)
soup = BeautifulSoup(movie_page, "html.parser")

# print(soup.find(name="h3", class_="title").getText())

movie_titles = soup.find_all(name="h3", class_="title")
# print(movie_titles)
name_movies = [name.getText() for name in movie_titles]
# for movie in movie_titles:
#     name = movie.getText()
#     name_movies.append(name)

# print(name_movies)
names_of_movies_inversed = name_movies[::-1]  # intoarcem lista de la nr 1 la nr 100
with open("movies_to_watch.txt", mode="w", encoding='utf-8') as file:
    for movie in names_of_movies_inversed:
        file.write(f"{movie}\n")
