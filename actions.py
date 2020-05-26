"""
all actions are stored here
"""


def action_handler(action, user, receiver):
    pass


def longsword(user, receiver):
    user.attack('str', '1d8', receiver)


def dash(user):
    user.sp = user.sp * 2


def evade(user):
    pass
