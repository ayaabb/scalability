from classes.user import User, posts


class SocialMediaPlatform:
    """Represents a social media platform.
    Attributes:
        users (list): A list of User objects representing registered users.
    """

    def __init__(self):
        self.users = []

    def register_user(self, username):
        """Registers a new user with the given username.
        param: username (str): The username of the user to register.
        """
        # O(n) - Linear time complexity due to iteration over the list of users (_is_username_taken method)
        if not self._is_username_taken(username):
            user = User(username)
            self.users.append(user)

    def _is_username_taken(self, username):
        """Checks if the given username is already taken.
        param: username (str): The username to check.
        Returns: bool: True if the username is taken, False otherwise.
        """
        # O(n) - Linear time complexity due to iteration over the list of users
        for user in self.users:
            if user.username == username:
                return True
        return False

    def get_user_by_username(self, username):
        """Retrieves the user object associated with the given username.
        param: username (str): The username of the user to retrieve.
        Returns: User or None: The user object if found, None otherwise.
        """
        # O(n) - Linear time complexity due to iteration over the list of users
        for user in self.users:
            if user.username == username:
                return user
        return None

    def generate_timeline(self, username):
        """Generates a timeline of posts from followed users for the given username.
        param: username (str): The username of the user for whom to generate the timeline.
        Returns: list: A list of posts from followed users.
        """
        # O(n*m) -  Where 'n' is the number of users the given user follows and 'm'
        # is the number of all the posts in the platform
        user = self.get_user_by_username(username)
        if not user:
            return []

        timeline = []
        for followed_user in user.following:
            for post in posts:
                if post['username'] == followed_user:
                    timeline.append(post)
        return timeline
