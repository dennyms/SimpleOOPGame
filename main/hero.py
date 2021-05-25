#Game OOP Sederhana
#Enjoy

import time
import random

class Hero:
  
  def __init__(self,name,hp,power,armor):
    self.name = name
    self.hp = hp
    self.power = power
    self.armor = armor
    
  def attack(self,enemy):
    print(self.name, "attack", enemy.name)
    enemy.hp -= self.power
    
  def deffense(self):
    print(self.name, "recovery", self.armor,"HP")
    self.hp += self.armor
    
  def powerup(self):
    print(self.name + "'s power up to", self.power + 1)
    self.power += 1
    
  def action(self,act,enemy):
    if act == 1:
      self.attack(enemy)
      if enemy.hp < 0:
        print(enemy.name, "HP: 0")
      else:
        print(enemy.name, "HP:",enemy.hp)
    elif act == 2:
      self.deffense()
      print(self.name, "HP:", self.hp)
    else:
      self.powerup()
      print(self.name, "Power:", self.power)
    print()
    
laila = Hero("Laila",50,6,3)
chang = Hero("Chang",55,3,6)
gung = Hero("Gung",50,5,5)

#PILIH HERO
print("List Hero:\n1. Laila\n2. Chang\n3. Gung")
print()
time.sleep(0.5)
my_hero_num = int(input("Choose number to be your Hero:"))
my_enemy_num = int(input("Choose number to be your Enemy:"))
time.sleep(0.5)
print()

if my_hero_num == 1:
  my_hero = laila
elif my_hero_num == 2:
  my_hero = chang
else:
  my_hero = gung
  
if my_enemy_num == 1:
  my_enemy = laila
elif my_enemy_num == 2:
  my_enemy = chang
else:
  my_enemy = gung
  
#PERKENALAN HERO  
print("Your Hero is",my_hero.name)
print("HP:", my_hero.hp); print("Power:", my_hero.power); print("Armor:", my_hero.armor)
print()
time.sleep(0.5)
print("Your enemy is",my_enemy.name)
print("HP:", my_enemy.hp); print("Power:", my_enemy.power); print("Armor:", my_enemy.armor)
print()

time.sleep(1.5)

#MULAI GAME
while my_hero.hp > 0 and my_enemy.hp > 0:

  print("--YOUR TURN--\n")
  print("Act:\n1. Attack\n2. Deffense\n3. Power up")
  my_act = int(input("Choose number:"))
  print()
  time.sleep(0.5)
  my_hero.action(my_act, my_enemy)
  time.sleep(1.5)
  
  if my_enemy.hp <= 0:
    break
  
  print("--ENEMY TURN--\n")
  enemy_act = random.randint(1,4)
  time.sleep(1)
  my_enemy.action(enemy_act, my_hero)
  time.sleep(1.5)

#GAME OVER
print("--GAME OVER--\n")
time.sleep(0.5)
if my_enemy.hp <= 0:
  print("You won!")
else:
  print("You lose!")
  
#Created by DMS
