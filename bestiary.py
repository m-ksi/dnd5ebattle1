from creature import Creature

sprite = 'succubus.png'
hp = 40
ac = 15
sp = 12
sp_type = 'flying'
att = (10, 20, 15, 8, 12, 20)
attacks = [['claws', 1, '1d8', 'slashing', 0, 'sounds/hit_knife.wav', 'sounds/miss_hit.wav'],
           ['fangs', 1, '1d6', 'piercing', 0, '', '']]
# name + attribute (number) + amount + type + advantage + sound + miss sound
sound = 'sounds/beinghit.mp3'


class Succubus(Creature):
    def __init__(self, n, s, h, a, spe, sp_t, atr, prof, aac, so):
        super().__init__(n, s, h, a, spe, sp_t, atr, prof, aac, so)


suc = Succubus('Lilith', sprite, hp, ac, sp, sp_type, att, 3, attacks, sound)

