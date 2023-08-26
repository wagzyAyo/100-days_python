countries_visited = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Dujon", "Lille", "Merseille", "Paris"]
    },
    {
        "country": "Germany",
        "visits": 12,
        "cities": ["Munich", "Berlin", "Dortmond", "Munchen"]
    },
]


def add_new_country(country, number_visited, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = number_visited
    new_country["cities"] = cities
    countries_visited.append(new_country)


add_new_country("Russia", 2, ["Moscow", "St peters burg"])

print(countries_visited)
