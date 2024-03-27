class ImprovedUser:
    """Represents an improved user object for a social media platform.
    Attributes:
        username (str): The username of the user.
        following (set): A set of usernames of users that this user is following.
        posts (list): A list of messages posted by this user.
    """

    def __init__(self, username):
        """Initializes an ImprovedUser object with the given username."""
        self.username = username
        self.following = set()
        self.posts = []

    def follow(self, other_user):  # O(1) - Constant time complexity for adding to a set
        """Adds the given user to the list of users being followed."""
        self.following.add(other_user)

    def post_message(self, message):  # O(1) - Constant time complexity for appending to a list
        """Posts the given message."""
        self.posts.append(message)
