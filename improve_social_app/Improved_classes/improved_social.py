from Improved_classes.improved_user import ImprovedUser


class ImprovedSocialMediaPlatform:
    def __init__(self):
        self.users = {}

    def register_user(self, username):  # o(1) average
        if self.users.get(username) is None:
            self.users[username] = ImprovedUser(username)

    def get_user_by_username(self, username):  # o(1) average
        if self.users.get(username) is not None:
            return self.users[username]
        print(username)
        return None

    def generate_timeline(self, username):  # o(n*m)
        user = self.get_user_by_username(username)
        if not user:
            return []
        timeline = []
        for followed_user in user.following:
            followed_user = self.get_user_by_username(followed_user)

            timeline += followed_user.posts
        return timeline
