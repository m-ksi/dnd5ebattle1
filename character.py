import arcade
from creature import Creature


sprite = 'char.png'
hp = 60
proficiency = 3
att = (18, 10, 16, 8, 10, 16)  # str dex con int wis cha
ac = 18
sp = 6
attacks = [['sword', 0, '1d8', 'slashing', 0, 'sounds/sword-hit.wav', 'miss_hit.wav']]
# name + attribute (number) + amount + type + advantage + sound + miss sound
bonus = ()
spell_slots = (0, 0, 0, 0, 0, 0, 0, 0, 0)


class Character(Creature):
    def __init__(self, n, s, h, a, spe, sp_t, atr, prof, aac, so):
        super().__init__(n, s, h, a, spe, sp_t, atr, prof, aac, so)


paladin = Character('Leroy', sprite, hp, ac, sp, 'walking', att, proficiency, attacks, 'sounds/suffers.mp3')

rogue = Character('Lenny', 'halfling_rogue.png', 40, 16, 5, 'walking', (10, 20, 14, 10, 10, 15), 3,
                  ['knife', 'push'], 'sounds/suffers.mp3')
