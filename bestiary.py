from creature import Creature
import actions

sprite = 'succubus.png'
hp = 40
ac = 15
sp = 12
sp_type = 'flying'
att = {'str': 10, 'dex': 20, 'con': 15, 'int': 8, 'wis': 12, 'cha': 20}
attacks = actions.ActionList([actions.claws])
# name + attribute (number) + amount + type + advantage + sound + miss sound
sounds = {'hurt': 'sounds/beinghit.mp3'}


class Succubus(Creature):
    def __init__(self, n, s, c, h, a, spe, sp_t, atr, prof, aac, so):
        super().__init__(n, s, c, h, a, spe, sp_t, atr, prof, aac, so)


suc = Succubus('Lilith', sprite, (5, 0), hp, ac, sp, sp_type, att, 3, attacks, sounds)

