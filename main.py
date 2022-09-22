import random
from bestiary import monsters, weapons, weapon_rarities
from def_color_console import *

hp = 0
coins = 0
damage = 0


# инициализация игры
def initGame(init_hp, init_coins, init_dmg):
    global hp
    global coins
    global damage

    hp = init_hp
    coins = init_coins
    damage = init_dmg
    prCyan('Ты отправился в темный, страшный лес, говорят там можно разбогатеть или умереть')
    # функц показывает статы
    show_state()


def gameLoop():
    situation = random.randint(0, 6)

    if situation == 0:
        meet_shop()
    elif situation == 1:
        meetMonster()
    else:
        input('Блуждаю...')


def show_state():
    print(f'У тебя {hp} жизней, {coins} монет и {damage} урона.')


def show_hp():
    print('У тебя', hp, 'жизней')


def show_coins():
    print('У тебя', coins, 'монет')


def show_damage():
    print('У тебя', damage, 'урона')


# встретили торговца
def meet_shop():
    global hp
    global coins
    global damage

    # можем ли что нибудь купить
    # если стоимость больше чем монет то досвидос
    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            show_coins()
            return True
        print('У тебя не достаточно монет!')
        return False

    # уровень оружия, урон
    weapon_lvl = random.randint(1, len(weapon_rarities))
    weapon_dmg = random.randint(1, 4) * weapon_lvl

    # редкость оружия
    weapon_rarity = weapon_rarities[weapon_lvl - 1]

    # стоимость оружия, рандомное значение умноженый на ур оружия
    weapon_cost = random.randint(3, 10) * weapon_lvl

    # оружие, которое предложит торговец
    weapon = random.choice(weapons)

    one_hp_cost = 5
    three_hp_cost = 12

    prGreen('Вы стретили торговца!')
    show_state()

    while input('Что ты будешь делать(зайти/уйти):').lower() == 'зайти':
        print('1) одно очко здоровья -', one_hp_cost, 'монет')
        print('2) три очка здоровья -', three_hp_cost, 'монет')
        print(f'3) {weapon_rarity} {weapon} - {weapon_cost} монет.')

        choice = input('Что будешь покупать? ')
        if choice == '1':
            if buy(one_hp_cost):
                hp += 1
                show_hp()
        elif choice == '2':
            if buy(three_hp_cost):
                hp += 3
                show_hp()
        elif choice == '3':
            if buy(weapon_cost):
                damage = weapon_dmg
                show_damage()
        else:
            print('Не нравится, не покупай!')


# встретили монстра
def meetMonster():

    global hp
    global coins

    # сложность врагов
    monster_lvl = random.randint(1, 5)
    monster_hp = monster_lvl
    monster_dmg = monster_lvl * 2 - 1
    monster = random.choice(monsters)

    prYellow("Ты встретил монстра - {0}, у него {1} уровень, {2} жизней и {3} урона.".format(monster, monster_lvl, monster_hp,
                                                                                        monster_dmg))
    show_state()

    while monster_hp > 0:
        choice = input("Что будешь делать (атака/бег): ").lower()

        if choice == "атака":
            monster_hp -= damage
            print("Ты ударил монстра и у него осталось", monster_hp, "жизней.")
        elif choice == "бег":
            chance = random.randint(0, monster_lvl)
            if chance == 0:
                prGreen("Тебе удалось сбежать с поля боя!")
                break
            else:
                print("Монстр легко догнал тебя...YOU DIED.")
                prRed("YOU DIED")
        else:
            continue

        if monster_hp > 0:
            hp -= monster_dmg
            print("Монстр атаковал и у тебя осталось", hp, "жизней.")

        if hp <= 0:
            prRed("YOU DIED")
            break
    else:
        loot = random.randint(0, 2) + monster_lvl
        coins += loot
        print("Тебе удалось одолеть монстра, за что ты получил", loot, "монет.")
        show_coins()


# передаем аргументы хп, coins, dmg (читер)
initGame(5, 10, 3)

while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала (да/нет): ").lower() == "да":
            initGame(3, 5, 1)
        else:
            break


