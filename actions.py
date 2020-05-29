"""
all actions are stored here
"""
from effects import *
import arcade

"""one_square_reach = ['w_longsword', 'w_claws', 'w_knife']
two_square_reach = ['w_spear']


def action_target_helper(action):
    if str(action.__name__)[0] == 'c':
        return 0
    elif str(action.__name__) in one_square_reach:
        return 1
    elif str(action.__name__) in two_square_reach:
        return 2"""


"""def action_handler(action, user, receiver=None, target_x=None, target_y=None):
    if str(action.__name__)[0] == 'w' or str(action.__name__) == 'push':
        action(user, receiver)
    elif str(action.__name__)[0] == 'c':
        action(user)"""


def action_handler(action, user, receiver=None):
    if action.target == 'self':
        action.function(user)
    elif action.target == 'enemy' or 'any_bs':
        s1 = action.sound['hit']
        s2 = action.sound['miss']
        action.function(user, receiver, s1, s2)


def w_longsword(user, receiver, s1, s2):
    user.attack('str', '1d8', receiver, "slashing", s1, s2)


def w_claws(user, receiver, s1, s2):
    user.attack('dex', '1d8', receiver, "slashing", s1, s2)


def w_knife(user, receiver, s1, s2):
    user.attack('dex', '1d4', receiver, "piercing", s1, s2)


def c_dash(user):
    user.effects.add_effect(dash)
    user.sp += user.sp_max


def c_evade(user):
    user.effects.add_effect(evasion)


def w_push(user, receiver):
    pass


class Action:
    def __init__(self, target, ico, sound, is_attack: bool, function, reach=None, max_reach=None):
        self.target = target  # self or enemy or ally or any but self or any or coordinate
        self.icon = ico  # icon
        try:
            self.sound = {'hit': arcade.load_sound(sound['hit']), 'miss': arcade.load_sound(sound['miss'])}
        except KeyError:
            self.sound = {}
        self.is_attack = is_attack  # attack or full action
        self.function = function
        self.reach = reach
        if max_reach is not None:
            self.max_reach = max_reach
        else:
            self.max_reach = reach


class ActionList:
    def __init__(self, a_list):
        self.action_list = a_list
        self.att_list = []
        self.make_att_list()

    def make_att_list(self):
        for a in self.action_list:
            if a.is_attack:
                self.att_list.append(a)

    def load_actions(self):
        return self.action_list

    def load_attacks(self):
        self.make_att_list()
        return self.att_list


longsword = Action('enemy', 'icons/w_longsword.png', {'hit': 'sounds/sword-hit.wav', 'miss': 'sounds/miss_hit.wav'}, True, w_longsword, 1)

claws = Action('enemy', 'icons/w_claws.png', {'hit': 'sounds/hit_knife.wav', 'miss': 'sounds/miss_hit.wav'}, True, w_claws, 1)

knife = Action('enemy', 'icons/w_knife.png', {'hit': 'sounds/hit_knife.wav', 'miss': 'sounds/miss_hit.wav'}, True, w_knife, 1)

push = Action('any_bs', 'icons/push.png', {'hit': 'sounds/hit_knife.wav', 'miss': 'sounds/miss_hit.wav'}, True, w_push, 1)

dash = Action('self', 'icons/dash.png', {}, False, c_dash, 0)
