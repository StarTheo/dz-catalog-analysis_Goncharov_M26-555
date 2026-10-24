"""Анализ каталога фильмов"""

import math

# Список фильмов с оценками из блока "Исходные данные"
movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]

# ----- Этап 1. Разминка: Переменные, числа, math


def average_rating(movies):
    """Средняя оценка по каталогу, округлённая до одного знака."""
    sum_mark = 0
    for movie in movies:
        sum_mark += movie["rating"]
    return round(sum_mark / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж (возраст самого старого,
    возраст самого нового, средний возраст)."""
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)


def duration_in_hours(minutes):
    """Возвращает строкy c переведёнными минутами
    в формат 'ЧЧч ММм'."""
    hours = minutes // 60
    minutes_after_hours = minutes % 60
    return f"{hours}ч {minutes_after_hours}м"


# ----- Этап 2. Условия и match


def rating_tier(rating):
    """Возвращает категорию-отзыв по оценке."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 5:
        return "хорошо" if rating >= 7 else "средне"
    else:
        return "слабо"


def decade_label(year):
    """Возвращает категорию-возраст по году выпуска."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# ----- Этап 3. Циклы


def print_non_comedy_titles(movies):
    """Возвращает наименования фильмов, которые не относятся к жанру комедии"""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_movie(movies, target_rating=9.0):
    """"""
    found = None
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > target_rating:
            found = movies[i]
            print(f"Первый шедевр в списке: {found['title']} ({found['rating']})")
            break
        i += 1
    else:
        print("Шедевров не найдено")
    return found


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# ----- Вывод для проверки
if __name__ == "__main__":
    print(average_rating(movies))
    print(catalog_age_stats(movies))
    print(duration_in_hours(155))
    print(rating_tier(8.6))
    print(decade_label(2016))
    print_non_comedy_titles(movies)
    find_first_movie(movies)
    find_first_movie(movies[:7])
    print(count_long_movies(movies))
