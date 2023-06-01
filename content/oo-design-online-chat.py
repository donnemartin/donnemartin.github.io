from abc import ABCMeta
from enum import Enum


class UserService(object):

    def __init__(self):
        self.users_by_id = {}  # key: user id, value: User

    def add_user(self, user_id, name, pass_hash):
        pass

    def remove_user(self, user_id):
        pass

    def add_friend_request(self, from_user_id, to_user_id):
        pass
