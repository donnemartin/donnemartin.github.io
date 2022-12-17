# Design an online chat

## Constraints and assumptions

* Assume we'll focus on the following workflows:
** Text conversations only
* Users
** Add a user
** Remove a user
** Update a user
** Add to a user's friends list
*** Add friend request
**** Approve friend request
**** Reject friend request
*** Remove from a user's friends list
* Create a group chat
** Invite friends to a group chat
** Post a message to a group chat
* Private 1-1 chat
** Invite a friend to a private chat
** Post a meesage to a private chat
* No need to worry about scaling initially

```
class UserService(object):

    def __init__(self):
        self.users_by_id = {}  # key: user id, value: User

    def add_user(self, user_id, name, pass_hash):  # ...
    def remove_user(self, user_id):  # ...
    def add_friend_request(self, from_user_id, to_user_id):  # ...
    def approve_friend_request(self, from_user_id, to_user_id):  # ...
    def reject_friend_request(self, from_user_id, to_user_id):  # ...

class User(object):

    def __init__(self, user_id, name, pass_hash):
        self.user_id = user_id
        self.name = name
        self.pass_hash = pass_hash
        self.friends_by_id = {}  # key: friend id, value: User
        self.friend_ids_to_private_chats = {}  # key: friend id, value: private chats
        self.group_chats_by_id = {}  # key: chat id, value: GroupChat
        self.received_friend_requests_by_friend_id = {}  # key: friend id, value: AddRequest
        self.sent_friend_requests_by_friend_id = {}  # key: friend id, value: AddRequest

    def message_user(self, friend_id, message):  # ...
    def message_group(self, group_id, message):  # ...
    def send_friend_request(self, friend_id):  # ...
    def receive_friend_request(self, friend_id):  # ...
    def approve_friend_request(self, friend_id):  # ...
    def reject_friend_request(self, friend_id):  # ...
```