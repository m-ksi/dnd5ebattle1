"""
all actions are stored here
"""
from effects import *


def action_handler(action, user, receiver=None, target_x=None, target_y=None):
    if str(action.__name__)[0] == 'w' or str(action.__name__) == 'push':
        action(user, receiver)
    if str(action.__name__)[0] == 'c':
        action(user)


def w_longsword(user, receiver):
    user.attack('str', '1d8', receiver, "slashing")


def c_dash(user):
    user.effects.add_effect(dash)


def c_evade(user):
    user.effects.add_effect(evasion)


def push(user, receiver):
    pass
