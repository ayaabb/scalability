from Improved_classes.improved_user import ImprovedUser


class ImprovedSocialMediaPlatform:
    """Represents an improved social media platform with efficient user management.
    Attributes:
        users (dict): A dictionary containing usernames as keys and ImprovedUser objects as values.
    """

    def __init__(self):
        self.users = {}

    def register_user(self, username):  # O(1) average - Constant time for dictionary access
        """Registers a new user with the given username.
        param: username (str): The username of the user to register.
        """
        if self.users.get(username) is None:
            self.users[username] = ImprovedUser(username)

    def get_user_by_username(self, username):  # O(1) average - Constant time for dictionary access
        """Retrieves the user object associated with the given username.
        param:  username (str): The username of the user to retrieve.
        Returns: ImprovedUser or None: The user object if found, None otherwise.
        """
        if self.users.get(username) is not None:
            return self.users[username]
        return None

    def generate_timeline(self, username):  # O(n * m') -- Where "n" is the number of users the given user follows and
        # "m'" is the average number of posts per followed user. Here, "m'" is less
        # than or equal to "m" in the previous implementation because "m'" represents
        # only the number of posts from followed users, whereas "m" represented all
        # the posts in the platform.
        """Generates a timeline of posts from followed users for the given username.
        param: username (str): The username of the user for whom to generate the timeline.
        Returns: list: A list of posts from followed users.
        """
        user = self.get_user_by_username(username)
        if not user:
            return []
        timeline = []
        for followed_user in user.following:
            followed_user = self.get_user_by_username(followed_user)
            timeline += followed_user.posts
        return timeline
