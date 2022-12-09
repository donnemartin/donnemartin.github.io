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
```