import arcade
import random
from effects import *
import mainfuncs


class Creature:

    def __init__(self, name, sprite, position, max_hp, ac, max_sp, sp_type, att, prof, attacks, sound):
        self.name = name
        self.sprite = arcade.Sprite(sprite, 8/3)
        self.position = []
        self.position.append(position[0])
        self.position.append(position[1])
        self.max_hp = int(max_hp)  # max health
        self.hp = self.max_hp  # current health
        self.ac = ac  # armor class
        self.max_sp = max_sp  # full speed
        self.sp = self.max_sp  # current speed
        self.sp_type = sp_type  # type of speed (flying, walking, etc)
        self.proficiency = prof
        self.att = att  # attributes (str dex con int wis cha)
        self.actions = attacks
        # self.sound = sound  # dict of sounds
        self.sound = {'hurt': arcade.load_sound(sound['hurt'])}
        self.effects = EffectList()  # active effects
        self.adv = 0  # 0 for normal, 1 for adv to hit this char, 0 for evasion
        self.action = 1
        self.num_of_attacks = 3

    def attack(self, attr, damage, Enemy, d_type, s1, s2):
        if Enemy.ac < random.randrange(1, 20) + (self.att[attr] - 10) // 2 + self.proficiency:
            print(self.name, 'hits!')
            Enemy.receive_damage(self, damage, attr, d_type)
            # arcade.play_sound(self.actions.sound['hit'])
            Enemy.sound['hurt'].play(volume=0.2)
            s1.play(volume=0.2)
        else:
            print(self.name, 'misses!')
            s2.play(volume=0.2)
            # arcade.play_sound(self.actions.sound['miss'])

    def receive_damage(self, Enemy, damage, attr, d_type):
        t_damage = 0
        for i in (range(int(damage.split('d')[0]))):
            t_damage += random.randrange(1, int(damage.split('d')[1]))
        t_damage += (Enemy.att[attr] - 10) // 2
        print(self.name, 'hurt in', t_damage, 'damage')
        self.hp -= t_damage
        if self.hp <= 0:
            print(self.name, 'dies!')
            self.die()

    def die(self):
        pass

    def roll_init(self):
        i = random.randrange(1, 20) + ((self.att['dex'] - 10) // 2)
        return i

    def next_turn(self):
        self.sp = self.max_sp
        self.adv = 0
        self.action = 1
        self.effects.next_turn()


class CreatureList:

    def __init__(self, c_list):
        self.Creature_list = c_list

        self.init_list = []
        self.order = []

        self.sprites = None
        self.sprites = arcade.SpriteList()

        self.roll_init()

        self.assign_sprites()

        self.positions = []
        self.update_positions()

    def roll_init(self):
        for i in range(len(self.Creature_list)):
            self.init_list.append(self.Creature_list[i].roll_init())
        self.order = sorted(range(len(self.init_list)), key=lambda k: self.init_list[k], reverse=True)
        for i in range(len(self.order)): self.order[i] = self.order[i] + 1

    def assign_sprites(self):
        for c in self.Creature_list:
            sprite = c.sprite
            self.sprites.append(sprite)

    def get_creature(self, n):  # by index in main list by init order
        for i in range(len(self.order)):
            if n == self.order[i]:
                return self.Creature_list[i]
        return -1

    def next_turn(self, t):
        self.Creature_list[t].next_turn()

    def update_positions(self):
        self.positions = []
        for char in self.Creature_list:
            self.positions.append(char.position)

