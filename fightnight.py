class Hero:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, villain):
        print(f"{self.name} attacks {villain1.name}!\n{villain1.name} lost {hero1.power} health.")
        villain.health -= hero1.power

    def is_alive(self):
        return self.health > 0

class Goblin:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def spit(self, hero):
        print(f"{self.name} spits acid at {hero.name}.")
        print(f"{villain1.power} - {hero1.health}")
        hero.health -= villain1.power
        print(f"{hero1.name} now has {hero1.health}")

    def is_alive(self):
        return self.health > 0

villain1 = Goblin("Joker", 100, 10)
hero1 = Hero("Batman", 100, 10)

def main():
    while villain1.is_alive() and hero1.is_alive():
        # Hero and Villain stats
        print(f"{hero1.name} has {hero1.health} health and {hero1.power} power.")
        print(f"The {villain1.name} has {villain1.health} health and {villain1.power} power.")
        print("What do you want to do?")
        # Player picks hero or villain
        print("1. Become the Hero")
        print("2. Become the Villain")
        print("3. Quit game")
        user_input = input("> ")

        # Player output Batman or Joker
        if user_input == "1":
            print(f"You have chosen {hero1.name} 🦇")
            while hero1.is_alive():
                print("What would you like to do?")
                print("1. Attack Joker")
                print("2. Power up")
                print("3. Call the Justice League")
                action = input("> ")
                if action == "1":
                    hero1.attack(villain1)
                elif action == "2":
                    print(f"This power-up will take time, which gives the {villain1.name} time to attack!")
                    print(f"{hero1.name} now has a Joker Buster suit!")
                    hero1.power = 20
                    print(f"{hero1.name} power is now {hero1.power}")
                elif action == "3":
                    print("Justice League is on its way!")
                    break
                else:
                    print("Invalid input.")
        elif user_input == "2":
            print(f"You have chosen {villain1.name}")
            while villain1.is_alive():
                print("What would you like to do?")
                print("1. Spit acid at Batman")
                print("2. Call for more villains")
                action = input("> ")
                if action == "1":
                    villain1.spit(hero1)
                elif action == "2":
                    print(f"{villain1.name} has called for more villains who will arrive shortly.")
                    break
                else:
                    print("Invalid input.")
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input.")

main()