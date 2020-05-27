"""
classes for effects to work
"""


class Effect:

    def __init__(self, length, function):
        self.length = length
        self.activate = function

    def next_turn(self):
        if self.length > 0:
            self.length -= 1

    def activate(self, char):
        self.activate(char)


class EffectList:

    def __init__(self):
        self.e_list = []

    def add_effect(self, effect):
        self.e_list.append(effect)

    def next_turn(self):
        for effect in self.e_list:
            effect.next_turn()
            if effect.length == 0:
                self.e_list.remove(effect)

    def activate(self, char):
        for effect in self.e_list:
            effect.activate(char)


"""
all effects  here
"""


def e_dash(char):
    char.sp = char.sp + char.sp_max


dash = Effect(1, e_dash)


def e_advantage(char):
    char.adv = 1


advantage = Effect(1, e_advantage)  # easier to hit this char


def e_disadvantage(char):
    char.adv = -1


evasion = Effect(1, e_disadvantage)  # more difficult to hit this char
