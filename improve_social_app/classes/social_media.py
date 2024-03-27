from classes.user import User, posts


class SocialMediaPlatform:
    def __init__(self):
        self.users = []

    def register_user(self, username):  # o(n)
        if not self._is_username_taken(username):
            user = User(username)
            self.users.append(user)

    def _is_username_taken(self, username):  # o(n)
        for user in self.users:
            if user.username == username:
                return True
        return False

    def get_user_by_username(self, username):  # o(n)
        for user in self.users:
            if user.username == username:
                return user
        return None

    def generate_timeline(self, username):  # o(n^2)
        user = self.get_user_by_username(username)
        if not user:
            return []

        timeline = []
        for followed_user in user.following:
            for post in posts:
                if post['username'] == followed_user:
                    timeline.append(post)
        return timeline
