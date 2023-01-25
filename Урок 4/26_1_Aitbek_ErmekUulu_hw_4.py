import random
from random import randint, choice
from enum import Enum

class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    EXPLOSION = 4
    AGRESSION = 5

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass



class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            coefficient = random.randint(2, 5)
            boss.health -= self.damage * coefficient
            print(f'Warrior hits critically {self.damage * coefficient}')

class Spitfire(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.AGRESSION)

    def apply_super_power(self, boss, heroes):
        pass
        # if self.health > 0:
        #     for hero in heroes:
        #         if heroes.__health <= 0:
        #             hero.damage += 65
        #     print(f"Spitfire used agressive")

class Magic(Hero):
    def __init__(self, name, health, damage, boost):
        super().__init__(name, health, damage, SuperAbility.BOOST)
        self.__boost = boost

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            for hero in heroes:
                if hero.health > 0:
                    hero.damage += self.__boost
            print(f"Magic used boost")

class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            for hero in heroes:
                if hero.health > 0 and self != hero:
                    hero.health += self.__heal_points

class Bomber(Hero):
    def __init__(self, name, health, damage):
        super(Bomber, self).__init__(name, health, damage, SuperAbility.EXPLOSION)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            for hero in heroes:
                if hero.health <= 0:
                    hero.damage = 100
            print(f"Bomber exploded")


round_number = 0


def print_statistics(boss, heroes):
    print(f'ROUND {round_number} -------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)


def start_game():
    boss = Boss('Devil', 1000, 50)
    warrior = Warrior('Ahilles', 270, 10)
    doc = Medic('Sasha', 250, 5, 15)
    magic = Magic('Dambldor', 280, 15, 5)
    bomber = Bomber('OG', 200, 15)
    # spitfire = Spitfire('Jack', 300, 15)

    heroes = [warrior, doc, magic, bomber]

    print_statistics(boss, heroes)
    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()

# 9. Hacker, который будет через раунд забирать у Босса N-ое количество здоровья и переводить его одному из героев
# 15. Герой Bomber, когда босс убивает героя он взрывается и наносит боссу дополнительный урон в 100 единиц.
#  16. Spitfire - каждый раз когда босс убивает одного или нескольких героев то наш герой показывает  агрессию на 80 единиц