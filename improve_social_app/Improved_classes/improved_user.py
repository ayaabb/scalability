class ImprovedUser:
    def __init__(self, username):
        self.username = username
        self.following = set()
        self.posts = []

    def follow(self, other_user):  # o(1)
        self.following.add(other_user)

    def post_message(self, message):  # o(1)
        post = message
        self.posts.append(post)



