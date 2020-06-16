#Hier ist nochmal mein Python Abenteuer...
#Ich hatte ihnen das ja am Mitwoch schon per Mail geschickt,
#weil Microsoft Teams aus irgeneinem Grund nicht funktioniert hatte...

import random
import time

prefix = ['Stinking', 'Brave', 'Slimey', 'Cowardly', 'Beautiful', 'Ugly', 'Penetrating', 'Slashing', 'Vengeful', 
          'Heroic', 'Decapitating', 'Super', 'Smelly', 'Dark', 'Invisible', 'Incontinent', 'Grumpy', 'Rotting', 'Sexy', 
          'Joyful', 'Well...', 'Obvious', 'Dancing', 'Fearful', 'Outdated', 'Weak', 'Unwanted', 'Never-asked-for', 
         'Questionable', 'Solar', 'Pompous', 'Average', 'Boring', 'Salty', 'Spicey', 'Racy', 'Mildy Interesting', 
          'Vicious', "Bloody"]
name = ['Olaf', 'Goblin', 'Butterfly', 'Adahn', 'Hero', 'Villian', 'Princess', 'Zak-Zak', 'Grobi',
        'Decapitator', 'Skeletor', 'Link', 'Kirby', 'Mario', 'Imperator', 'Sith', 'Jedi', 'Conan', 'Jellyfish',
       'Huppa-Huppa', 'Terrorist', 'Trump', 'Putin', 'Wiener Schnitzel', 'Ferdinand', 'Captain', 'Failalot', 'Orbiter',
       'Peasant']
suffix = ['Doom', 'Vengerberg', 'Joy', 'Might', 'Greyskull', 'Berlin', 'Decapitation', 'Toad Island', 'Infinity',
          'Destruction', 'Desperation', 'Sex Appeal', 'Obamacare', 'Alderaan', 'Öhm', 'Excellence', 'Dance', 'Confusion',
          'Failure', 'Valium', 'Boring', 'Cabbage']

class Item:
    def __init__(self, name, cost, uses, damage, shield, description, haseffect):

        self.name = name
        self.cost = cost
        self.usesleft = uses
        self.attackdamage = damage
        self.shield = shield
        self.description = description
        self.hasEffect = haseffect

fists = Item("fists", 0, 100, 5, 0, "One puuuunch!", False)
sword = Item("sword", 150, 100, 18, 0, "Does extra attack damage", False)
healingPotion = Item("healing potion", 50, 1, 0, 0, "Oh it restores HP? Thanks captain obvious!", True)
shield = Item("shield", 50, 0, 0, 15, "Does what shields usually do", False)
nunchuck = Item("nunchuck", 100, 100, 8, 8, "Blocks attacks and does extra damage", False)
ak47 = Item("AK-47", 250, 100, 25, 0, "Super cool and does massive damage", False)
unoReverse = Item("Uno reverse card", 50, 1, 0, 0, "No u!", True)
egg = Item("egg", 25, 1, 0, 0, "Throw an egg into your opponent's face", True)
mysteryBox = Item("mystery box", 125, 0, 0, 0, "What could be inside? :o", False)
goldenApple = Item("golden apple", 75, 1, 0, 0, "Even tastier than they look", True)
diamondChestplate = Item("diamond chestplate", 100, 0, 0, 30, "Fancy and robust", False)
enchantedDiamondArmor = Item("enchanted diamond armor", 175, 0, 0, 60, "Cover me with diamonds", False)
sauronsRing = Item("sauron's ring", 75, 1, 0, 0, "One ring to rule them all", True)
allItems = [sword, nunchuck, ak47, egg, goldenApple, healingPotion, diamondChestplate, enchantedDiamondArmor, shield, sauronsRing, mysteryBox]
allItemNames = ["sword", "nunchuck", "AK-47", "egg", "golden apple", "healing potion", "diamond chestplate", "enchanted diamond armor", "shield", "sauron's ring", "mystery box"]

#EFFECTS FOR ITEMS

def healingPotionEff(fighter, opponent):
    fighter.health += 45
    print("*" + fighter.name + " drinks healing potion and gains +30HP*")
def unoReverseEff(fighter, opponent):
    print("*" + fighter.name + " takes a mysterious piece of paper out of his pocket...*")
    print(opponent.name + ": 'Are you going to attack already? Well... I guess it's my turn then!'")
    damage = random.randint(30, 35)*opponent.attackMultiplier
    print("*" + opponent.name + " attacks " + fighter.name + " and inflicts " + str(damage) + "HP...<*")
    print("*" + fighter.name + " shouts 'NO U' at " + opponent.name + " and reveals a Uno Reverse Card!" + opponent.name + "'s attack is mirrored back onto himself and inflicts " + damage + "HP damage*")
def eggEff(fighter, opponent):
    print("*" + fighter.name + " tosses egg into " + opponent.name + "'s face and inflicts 3HP damage. " + opponent.name + "'s sight is blured by the eggwhite in their face which makes his attacks slightly weaker*")
    opponent.attackMultiplier = 0.85
def mysteryBoxEff(fighter, opponent):
    fighter.items.append(random.choice(allItems))
def sauronEff(fighter, opponent):
    print("*" + fighter.name + " put's on sauron's ring which makes them invisible." + opponent.name + " is more likely to miss now*")
    opponent.missChance = 0.7
def appleEff(fighter, opponent):
    fighter.health += 30
    fighter.attackMultiplier += 0.3
    print("*" + fighter.name + " eats golden apple and gains more strength and extra HP*")

healingPotion.effect = healingPotionEff
egg.effect = eggEff
mysteryBox.effect = mysteryBoxEff
unoReverse.effect = unoReverseEff
sauronsRing.effect = sauronEff
goldenApple.effect = appleEff

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.items = [fists]
        self.health = health
        self.attackMultiplier = 1
        self.money = 300
    
    def attack(self, target):
        print("It's your turn! Select one of your items to attack / use.")
        time.sleep(1.5)
        for item in self.items:
            print(item.name + " " + item.description)
            time.sleep(0.2)

        found = False
        inp = str(input())
        for item in self.items:
            if(inp == item.name):
                found = True
                print("You selected " + item.name + "!")
                time.sleep(1)
                item.usesleft -= 1
                if(item.hasEffect):
                    item.effect(hero, villian)
                if(item.attackdamage > 0):
                    damage = round(item.attackdamage*hero.attackMultiplier)
                    print("*" + hero.name + " attacks " + villian.name + " using " + item.name + " and inflicts " + str(damage) + "HP damage*")
                    villian.health -= damage
                    time.sleep(3.5)
        if(not found):
            print("You don't have " + inp + " , using 'Fists' instead.")
            time.sleep(2.5)
            print("*" + hero.name + " attacks " + villian.name + " using " + fists.name + " and inflicts " + str(fists.attackdamage) + "HP damage*")
            time.sleep(3.5)
            villian.health -= fists.attackdamage

class Villian:
    def __init__(self, name, health):
        self.name = name
        self.items = []
        self.health = health
        self.attackMultiplier = 1
        self.attackdamage = 5
        self.missChance = 0.9

    def attack(self, target):
        damage = round(random.randint(20, 25)*self.attackMultiplier)
        if(random.randint(0, self.missChance*10) == 0):
            print("*" + self.name + " attacks but misses!*")
            time.sleep(2)
        else:
            print("*" + self.name + " attacks " + target.name + " and inflicts " + str(damage) + "HP damage*")
            target.health -= damage
            time.sleep(2.5)

def fight(hero, villian):
    #init
    if (mysteryBox in hero.items):
        print("Last chance to open your mystery box! Type yes to open")
        inp = input()
        if(inp == "yes"):
            openMysteryBox()

    for item in hero.items:
        hero.health *= 1+item.shield/100
    stop = True

    while(stop):
        for item in hero.items:
            if(item.usesleft <= 0):
                hero.items.remove(item)

        hero.attack(villian)
        if (villian.health <= 0):
            print("*" + hero.name + " has slain " + villian.name + "*")
            stop = False
        else:
            villian.attack(hero)
            if (hero.health <= 0):
                print("*" + villian.name + " has slain " + hero.name + "*")
                stop = False

hero = Hero(random.choice(prefix) + " " + random.choice(name) + " of " + random.choice(suffix), 100)
villian = Villian(random.choice(prefix) + " " + random.choice(name) + " of " + random.choice(suffix), 130)

#INTRO

print("Help our hero " + hero.name + " to free the princess from the evil villian " + villian.name + "!")
time.sleep(1)

#ITEM SHOP CODE

def openMysteryBox():
    stop = True
    while(stop):
        content = random.choice(allItems)
        if(not content in hero.items):
            stop = False
        
    if(content == mysteryBox):
        print("the mystery box contained... another mystery box! ._.")
        time.sleep(0.5)
        print("Do you want to open it? Type yes to open")
        inp = input()
        if(inp == "yes"):
            openMysteryBox()
    else:
        print("The mystery box contained " + content.name + "!")
        hero.items.append(content)
        time.sleep(1)

def shopSequence():
    print("*you enter the item shop*")
    time.sleep(1.5)
    print("Goblin vendor: Welcome to the item shop. We have everything you need to defeat " + villian.name + "!")
    time.sleep(2)
    print("*you've brought 300 coins with you. spend them wisely!*")
    time.sleep(2)
    print("*You can only buy one of each item. To buy something type it's name into the console, if you want to leave the shop type 'leave'*")
    time.sleep(4)
    for item in allItems:
        time.sleep(0.1)
        print(item.name + ", cost: " + str(item.cost) + ", description: " + item.description)
    stop = True
    while(stop):
        inp = input()
        inp = str(inp)
        if(inp == "leave"):
            print("*You left the shop*")
            stop = False
        elif(not inp in allItemNames):
            print("invalid selection!")
        elif(allItems[allItemNames.index(inp)] in hero.items):
            print("You already bought this.")
        elif(allItems[allItemNames.index(inp)].cost <= hero.money):
            hero.money -= allItems[allItemNames.index(inp)].cost
            hero.items.append(allItems[allItemNames.index(inp)])
            print("You bought " + inp + ". You have " + str(hero.money) + " coins left.")
        else:
            print("You don't have enough money to buy this!")
    if(len(hero.items) > 1):
        print("You now possess the following items:")
        for item in hero.items:
            print(item.name)
        if(mysteryBox in hero.items):
            print("Do you want to open your mystery box now? Type yes to open. You can still open it later.")
            inp = input()
            if(inp == "yes"):
                openMysteryBox()

#SHOP SEQUENCE
print("You walk past a small shop. Type yes if you want to enter")
inp = input()
if(str(inp) == "yes"):
    shopSequence()
#CONFIRM
print("Do you think you are prepared to fight " + villian.name + " now? Type yes to fight, type no to return to the shop.")
stop = True
while(stop):
    inp = input()
    if(inp == "no"):
        shopSequence()
        stop = False
    elif(inp == "yes"):
        stop = False
    else:
        print("not a valid input!")
time.sleep(1)
print("The fight beginns...")

#THE FIGHT
 
fight(hero, villian)