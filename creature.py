import arcade
import random


class Creature:

    def __init__(self, sprite, hp, ac, sp, sp_type, att, attacks, sound):
        self.sprite = sprite
        self.hp = hp  # health
        self.ac = ac  # armor class
        self.sp = sp  # speed
        self.sp_type = sp_type  # type of speed (on earth, air, etc)
        self.att = att  # attributes (str dex con int wis cha)
        self.attacks = attacks  # name + attribute (number) + amount + type + advantage + sound + miss sound
        self.sound = sound

    def attack(self, attack, Enemy):
        if Enemy.ac < random.randrange(1, 20) + (self.att(attack(1)) - 10) // 2:
            Enemy.receive_damage(attack, self)
            # play hit sound
            # play suffer sound
        else:
            pass  # play miss sound

    def receive_damage(self, attack, Enemy):
        damage = 0
        for i in range(int(attack(2).split('d')[0])):
            damage += random.randrange(1, int(attack(2).split('d')[1]))
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        pass
