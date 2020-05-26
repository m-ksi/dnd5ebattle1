import arcade
from creature import Creature


sprite = 'char.png'
hp = 60
att = (18, 10, 16, 8, 10, 16)  # str dex con int wis cha
ac = 18
sp = 6
attacks = [['sword', 0, '1d8', 'slashing', 0, 'sounds/sword-hit.wav', 'miss_hit.wav']]
# name + attribute (number) + amount + type + advantage + sound + miss sound
bonus = ()
spell_slots = (0, 0, 0, 0, 0, 0, 0, 0, 0)


class Character(Creature):
    def __init__(self, n, s, h, a, spe, sp_t, atr, aac, so):
        super().__init__(n, s, h, a, spe, sp_t, atr, aac, so)


char = Character('Leroy', sprite, hp, ac, sp, 'walking', att, attacks, 'sounds/suffers.mp3')
