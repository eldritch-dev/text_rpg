from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


# Cast Elemental Magic
fire = Spell("Fire", 10, 101, "elemental")
thunder = Spell("Thunder", 8, 80, "elemental")
blizzard = Spell("Blizzard", 10, 101, "elemental")
lightning = Spell("Lightning", 14, 150, "elemental")
meteor = Spell("Meteor", 20, 200, "elemental")

# Cast Divine Magic
healing = Spell("Healing", 15, 120, "divine")
major_healing = Spell("Major Healing", 20, 180, "divine")


# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
super_elixir = Item("Super Elixir", "elixir", "Fully restores party's HP/MP", 9999)

dragon_fire = Item("Dragon Fire", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, lightning, meteor, healing, major_healing]
player_items = [{"item": potion, "quantity": 15}, {"item": hi_potion, "quantity": 5},
                {"item": super_potion, "quantity": 3}, {"item": elixir, "quantity": 2},
                {"item": super_elixir, "quantity": 1}, {"item": dragon_fire, "quantity": 1}]

# Instantiate People
player1 = Person("Valos: ", 3300, 65, 60, 34, player_spells, player_items)
player2 = Person("Kirie: ", 4190, 65, 60, 34, player_spells, player_items)
player3 = Person("Irile: ", 3030, 65, 60, 34, player_spells, player_items)
enemy = Person("Irikesh", 1200, 65, 45, 25, [], [])

players = [player1, player2, player3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("\n\n")
    print("NAME                 HP                                  MP")
    for player in players:
        player.get_stats()

    print("\n")

    for player in players:

        player.choose_action()
        choice = input("    Choose action:")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose Spell:")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough magic points\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "divine":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "elemental":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + " None left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixir":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage"+ bcolors.ENDC)
    enemy.choice = 1

    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("Enemy attacks you for", enemy_dmg)

    print("~~~~~~~~~~~~~~")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "The enemy has defeated you!" + bcolors.ENDC)
        running = False