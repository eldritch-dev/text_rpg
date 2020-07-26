from classes.game import Person, bcolors
from classes.magic import Spell

# Cast Elemental Magic
fire = Spell("Fire", 10, 101, "elemental")
thunder = Spell("Thunder", 8, 80, "elemental")
blizzard = Spell("Blizzard", 10, 101, "elemental")
lightning = Spell("Lightning", 14, 150, "elemental")
meteor = Spell("Meteor", 20, 200, "elemental")

# Cast Divine Magic
healing = Spell("Healing", 15, 120, "divine")
major_healing = Spell("Major Healing", 20, 180, "divine")

# Instantiate People
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, lightning, meteor, healing, major_healing])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Spell:")) - 1


        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough magic points\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy.choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks you for", enemy_dmg)

    print("~~~~~~~~~~~~~~")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "The enemy has defeated you!" + bcolors.ENDC)
        running = False