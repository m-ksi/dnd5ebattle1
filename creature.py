import arcade
import random


class Creature:

    def __init__(self, name, sprite, max_hp, ac, max_sp, sp_type, att, prof, attacks, sound):
        self.name = name
        self.sprite = arcade.Sprite(sprite, 8/3)
        self.max_hp = max_hp  # max health
        self.hp = self.max_hp  # current health
        self.ac = ac  # armor class
        self.max_sp = max_sp  # full speed
        self.sp = self.max_sp  # current speed
        self.sp_type = sp_type  # type of speed (on earth, air, etc)
        self.proficiency = prof
        self.att = att  # attributes (str dex con int wis cha)
        self.attacks = attacks  # name + attribute (number) + amount + type + advantage + sound + miss sound
        self.sound = sound  # suffering damage

    def attack(self, attack, Enemy):
        if Enemy.ac < random.randrange(1, 20) + (self.att(attack(1)) - 10) // 2 + self.proficiency:
            Enemy.receive_damage(attack, self)
            arcade.play_sound(self.attacks[0][5])
            arcade.play_sound(self.sound)
        else:
            arcade.play_sound(self.attacks[0][6])

    def receive_damage(self, attack, Enemy):
        damage = 0
        for i in range(int(attack(2).split('d')[0])):
            damage += random.randrange(1, int(attack(2).split('d')[1]))
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        pass

    def roll_init(self):
        i = random.randrange(1, 20) + ((self.att[1] - 10) // 2)
        return i

    def next_turn(self):
        self.sp = self.max_sp


class CreatureList:

    def __init__(self, c_list):
        self.Creature_list = c_list

        self.init_list = []
        self.order = []

        self.sprites = None
        self.sprites = arcade.SpriteList()

        self.roll_init()

        self.assign_sprites()

    def roll_init(self):
        for i in range(len(self.Creature_list)):
            self.init_list.append(self.Creature_list[i].roll_init())
        self.order = sorted(range(len(self.init_list)), key=lambda k: self.init_list[k], reverse=True)
        for i in range(len(self.order)): self.order[i] = self.order[i] + 1

    def assign_sprites(self):
        for c in self.Creature_list:
            sprite = c.sprite
            self.sprites.append(sprite)

    def get_creature(self, n):
        for i in range(len(self.order)):
            if n == self.order[i]:
                return self.Creature_list[i]
        return -1

    def next_turn(self):
        for c in self.Creature_list:
            c.next_turn()


