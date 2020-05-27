import arcade
from creature import Creature


sprite = 'char.png'
hp = 60
proficiency = 3
att = {'str': 18, 'dex': 10, 'con': 16, 'int': 8, 'wis': 10, 'cha': 16}
ac = 18
sp = 6
attacks = ['w_longsword', 'push']
# name + attribute (number) + amount + type + advantage + sound + miss sound
bonus = ()
spell_slots = (0, 0, 0, 0, 0, 0, 0, 0, 0)


class Character(Creature):
    def __init__(self, n, s, h, a, spe, sp_t, atr, prof, aac, so):
        super().__init__(n, s, h, a, spe, sp_t, atr, prof, aac, so)


paladin = Character('Leroy', sprite, hp, ac, sp, 'walking', att, proficiency, attacks, 'sounds/suffers.mp3')

rogue = Character('Lenny', 'halfling_rogue.png', 40, 16, 5, 'walking',
                  {'str': 10, 'dex': 20, 'con': 14, 'int': 10, 'wis': 10, 'cha': 15}, 3, ['w_knife', 'push'],
                  'sounds/suffers.mp3')
