class User:
    def __init__(self, username):
        self.username = username
        self.following = []

    def follow(self, other_user):  # o(n)
        if other_user not in self.following:
            self.following.append(other_user)

    def post_message(self, message):  # o(1)
        post = {'username': self.username, 'message': message}
        posts.append(post)


# Assume posts are stored in a global list of dictionaries
posts = []
