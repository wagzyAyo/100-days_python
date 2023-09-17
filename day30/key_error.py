facebbok_post = [
    {"Likes": 21, "Comment": 2},
    {"Likes": 13, "Comment": 2, "Shares": 1},
    {"Likes": 33, "Comment": 8, "Shares": 3},
    {"Shares": 2, "Comment": 4},
    {"Comment": 1, "Shares": 1},
    {"Likes": 19, "Shares": 3}
]


total_likes = 0

for post in facebbok_post:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        total_likes = total_likes + 0

print(total_likes)
