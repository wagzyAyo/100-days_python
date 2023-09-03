class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.follower = 0


# Naming a class in python all first word start with capital PASCAL CASE
user_1 = User('001', 'Ayomide')
print(user_1.name)

