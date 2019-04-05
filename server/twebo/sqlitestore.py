# Copyright (C) 2019

from typing import Dict, List
from twebo.store import Store


class SqliteStore(Store):
    """Sqlite3 storage implementation."""

    def __init__(self, url: str):
        """Constructor.

        :param url: Persistent storage URL."""
        self._url = url
        return

    def new_user(self, username: str, password: bytes, nickname: str) -> None:
        """Create new user.

        :param username: Full name for user.
        :param password: Hashed password for user.
        :param nickname: User's default nick name."""
        pass

    def disable_user(self, username: str) -> None:
        """Mark user's account as disabled, preventing login.

        :param username: Full name for user."""
        pass

    def enable_user(self, username: str) -> None:
        """Mark user's account as enabled, enabling login.

        :param username: Full name for user."""
        pass

    def reset_password(self, username: str, password: bytes) -> None:
        """Reset user's password.

        :param username: Full name for user.
        :param password: Hashed new password for user."""
        pass

    def delete_user(self, username: str) -> None:
        """Delete a user.

        :param username: Full name for user."""
        pass

    def set_presence(self, username: str, status: str) -> None:
        """Update user's presence status.

        :param username: Full name for user.
        :param status: One of 'typing', 'active', 'idle', 'offline'."""
        pass

    def new_group_subscription(self, username: str, group: str) -> None:
        """Create new group subscription for user.

        :param username: Full name for user.
        :param group: Group name."""
        pass

    def delete_group_subscription(self, username: str, group: str) -> None:
        """Delete group subscription for user.

        :param username: Full name for user.
        :param group: Group name."""
        pass

    def get_subscribers_for_group(self, group: str) -> List[str]:
        """Return list of users who subscribe to this group.

        :param group: Group name.
        :returns: List of subscribed usernames."""
        pass

    def get_group_subscriptions_for_user(self, username: str) -> List[str]:
        """Return list of groups subscribed by this user.

        :param username: Full name of user.
        :returns: List of subscribed groups."""
        pass

    def new_message(self, message: dict) -> None:
        """Insert new published message.

        :param message: Message dictionary."""
        pass

    def get_message(self, message_id: str) -> dict:
        """Return message by identifier.

        :param message_id: Message identifier.
        :returns: Message dictionary."""
        pass

    def new_delivery(self, username: str, group: str, message_id: str) -> None:
        """Insert new delivery record.

        :param username: Full name of target user.
        :param group: Group name.
        :param message_id: Identifier of delivered message."""
        pass

    def mark_delivery_as_read(self, username: str, message_id: str) -> None:
        """Mark delivery as read by user.

        :param username: Full name of user.
        :param message_id: Identifier of message."""
        pass

    def mark_thread_as_killed(self, username: str, message_id: str) -> None:
        """Mark message as thread-killed.

        :param username: Full name of user.
        :param message_id: Identifier of message in thread."""
        pass

    def get_new_deliveries_for_user(self, username: str) -> List[str]:
        """Return list of undelivered messages for user.

        :param username: Full name of user.
        :returns: List of message identifiers."""
        pass

    def new_presence_subscription(self, subscriber: str, target: str) -> None:
        """Insert new presence subscription.

        :param subscriber: Full name of subscribing user.
        :param target: Full name of target user."""
        pass

    def delete_presence_subscription(self,
                                     subscriber: str,
                                     target: str) -> None:
        """Delete presence subscription.

        :param subscriber: Full name of subscribing user.
        :param target: Full name of target user."""
        pass

    def get_subscribed_presence(self, subscriber: str) -> Dict[str, str]:
        """Return mapping of username to presence for all subscribed users.

        :param subscriber: Full name of subscribing user.
        :returns: Dictionary of presence status, indexed by username."""
        pass
