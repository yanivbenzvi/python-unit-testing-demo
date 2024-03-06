import logging

logger = logging.getLogger(__name__)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, username):
        for user in self.users:
            if user.username == username:
                self.users.remove(user)
                return True
        return False

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
        logger.warning(f"User with username {username} not found")
        return None
