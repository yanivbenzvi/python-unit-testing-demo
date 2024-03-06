from unittest.mock import patch

import pytest

from src.user import UserManager, User


# Test case 1: Given a new user, when adding the user, then the user should be in the user list
def test_user_manager_add_user():
    # Given
    user_manager = UserManager()
    user = User("john_doe", "john@example.com")

    # When
    user_manager.add_user(user)

    # Then
    assert user in user_manager.users


# Test case 2: Given an existing user, when removing the user, then the user should be removed from the user list
def test_user_manager_remove_user():
    # Given
    user_manager = UserManager()
    user = User("jane_doe", "jane@example.com")
    user_manager.add_user(user)

    assert user in user_manager.users

    # When
    user_manager.remove_user("jane_doe")

    # Then
    assert user not in user_manager.users


# Test case 3: Given an existing username, when getting the user by username,
# then the correct user object should be returned
def test_user_manager_get_user_by_username():
    # Given
    user_manager = UserManager()
    user = User("alice", "alice@example.com")
    user_manager.add_user(user)

    # When
    retrieved_user = user_manager.get_user_by_username("alice")

    # Then
    assert retrieved_user == user


# Test case 4: Given a non-existent username, when getting the user by username, then None should be returned
@patch('src.user.logging.warning')
def test_user_manager_get_non_existent_user(mock_warning):
    # Given
    user_manager = UserManager()

    # When
    retrieved_user = user_manager.get_user_by_username("non_existent_user")

    # Then
    assert retrieved_user is None
    mock_warning.assert_called_once_with("User with username non_existent_user not found")
