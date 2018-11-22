import random


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkH = atk-10
        self.atkL = atk+10
        self.df = df
        self.magic = magic
        self.action = ['Attack', 'Magic']

    def generate_dmg(self):
        return random.randrange(self.atkH, self.atkL)

    def generate_spell_dmg(self, i):
        mgl = self.magic[i]['damage'] - 5
        mgh = self.magic[i]['damage'] + 5
        return random.randrange(mgl, mgh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxHp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxMp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]['name']

    def get_spell_mp_cost(self, i):
        return self.magic[i]['cost']

    def choose_action(self):
        i = 1
        print('Actions')
        for item in self.action:
            print(str(i) + ':' + item)
            i += 1

    def choose_spell(self):
        i = 1
        print('Spells')
        for item in self.magic:
            print(str(i) + ':' + item['name'], 'cost : ', item['cost'])
            i += 1

