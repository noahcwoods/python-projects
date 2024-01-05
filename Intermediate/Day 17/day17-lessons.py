class User:
    def __init__(self, id=0, name="John"):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1




user1 = User(1, 'John')
user2 = User(2, "Jenkins")

user1.follow(user2)
print(user1.following)
print(user2.followers)