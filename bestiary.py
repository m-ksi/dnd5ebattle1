from creature import Creature

sprite = 'succubus.png'
hp = 40
ac = 15
sp = 60
sp_type = 'flying'
att = (10, 20, 15, 8, 12, 20)
attacks = [['claws', 1, '1d8', 'slashing', 0, '', ''],
           ['fangs', 1, '1d6', 'piercing', 0, '', '']]
# name + attribute (number) + amount + type + advantage + sound + miss sound
sound = ''


class Succubus(Creature('Succubus', sprite, hp, ac, sp, sp_type, att, attacks, sound)):
    pass
