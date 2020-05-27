import arcade
import random
from effects import *
from grid import chars_grid
import mainfuncs


class Creature:

    def __init__(self, name, sprite, max_hp, ac, max_sp, sp_type, att, prof, attacks, sound):
        self.name = name
        self.sprite = arcade.Sprite(sprite, 8/3)
        self.max_hp = max_hp  # max health
        self.hp = self.max_hp  # current health
        self.ac = ac  # armor class
        self.max_sp = max_sp  # full speed
        self.sp = self.max_sp  # current speed
        self.sp_type = sp_type  # type of speed (flying, walking, etc)
        self.proficiency = prof
        self.att = att  # attributes (str dex con int wis cha)
        self.attacks = attacks
        self.sound = sound  # suffering damage
        self.effects = EffectList()  # active effects
        self.adv = 0  # 0 for normal, 1 for adv to hit this char, 0 for evasion

    def attack(self, attr, damage, Enemy, d_type):
        if Enemy.ac < random.randrange(1, 20) + (self.att(attr) - 10) // 2 + self.proficiency:
            Enemy.receive_damage(damage, d_type)
            # arcade.play_sound(self.attacks[0][5])
            # arcade.play_sound(Enemy.sound)
        else:
            pass
            # arcade.play_sound(self.attacks[0][6])

    def receive_damage(self, damage, d_type):
        t_damage = 0
        for i in (range(int(damage.split('d')[0]) - 1)):
            damage += random.randrange(1, int(damage.split('d')[1]))
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        pass

    def roll_init(self):
        i = random.randrange(1, 20) + ((self.att['dex'] - 10) // 2)
        return i

    def next_turn(self):
        self.sp = self.max_sp
        self.adv = 0
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

    def next_turn(self):
        for c in self.Creature_list:
            c.next_turn()

    def if_dies(self):
        for c in self.Creature_list:
            if c.hp <= 0:
                n = self.Creature_list.index(c)
                [row, column] = mainfuncs.find_char(n + 1, chars_grid)
                print(row, column)
                order = self.order[n]
                self.kill(c, row, column, order)
                # chars_grid[row][column] = 0
                # self.Creature_list.remove(c)

    def kill(self, char, row, column, order):
        self.Creature_list.remove(char)
        print('Creature_list in class:', self.Creature_list)
        self.sprites.remove(char.sprite)
        chars_grid[row][column] = 0
        self.fix_init(order)

    def fix_init(self, order):
        self.order.remove(order)
        for i in range(len(self.order)):
            if self.order[i] > order:
                self.order[i] -= 1
        print('order in class:', self.order)

