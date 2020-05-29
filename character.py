import arcade
from creature import Creature
import actions

sprite = 'char.png'
hp = 60
proficiency = 3
att = {'str': 18, 'dex': 10, 'con': 16, 'int': 8, 'wis': 10, 'cha': 16}
ac = 18
sp = 6
attacks = actions.ActionList([actions.longsword, actions.push, actions.dash])
bonus = []


class Character(Creature):
    def __init__(self, n, s, c, h, a, spe, sp_t, atr, prof, aac, so):
        super().__init__(n, s, c, h, a, spe, sp_t, atr, prof, aac, so)


paladin = Character('Leroy', sprite, (1, 8), hp, ac, sp, 'walking', att, proficiency, attacks, {'hurt': 'sounds/suffers.mp3'})

rogue = Character('Lenny', 'halfling_rogue.png',
                  (5, 11), 40, 16, 5, 'walking',
                  {'str': 10, 'dex': 20, 'con': 14, 'int': 10, 'wis': 10, 'cha': 15},
                  3, actions.ActionList([actions.knife, actions.push, actions.dash]),
                  {'hurt': 'sounds/beinghit.mp3'})
