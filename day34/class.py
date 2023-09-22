class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Naming a class in python all first word start with capital PASCAL CASE
user_1 = User('001', 'Ayomide')
user_2 = User("002", "Angela")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
