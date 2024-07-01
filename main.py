import random

def get_name():
  name = input("What is your charecter's name? ")
  return name
print(f"🎲Welcome to the game, {get_name()}🎲")

print("Rolling four dice.... ")
def sum_of_four_six_sided_dice_with_lowest_dropped():
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  dice3 = random.randint(1, 6)
  dice4 = random.randint(1, 6)

  min_dice = min(dice1, dice2, dice3, dice4)
  roll = dice1 + dice2 + dice3 + dice4 - min_dice

  return roll

strength = sum_of_four_six_sided_dice_with_lowest_dropped()
dexterity = sum_of_four_six_sided_dice_with_lowest_dropped()
constitution = sum_of_four_six_sided_dice_with_lowest_dropped()
intelligence = sum_of_four_six_sided_dice_with_lowest_dropped()
wisdom = sum_of_four_six_sided_dice_with_lowest_dropped()
charisma = sum_of_four_six_sided_dice_with_lowest_dropped()

print("HERE ARE YOU STATS TO START WITH")
print(f"Strength: {strength}")
print(f"Dexterity: {dexterity}")
print(f"Constitution: {constitution}")
print(f"Intelligence: {intelligence}")
print(f"Wisdom: {wisdom}")
print(f"Charisma: {charisma}\n")
print("Let's see them with modifiers!")

def get_ability_modifier(strength, dexterity, constitution, intelligence, wisdom, charisma):
  mod_strength = (strength - 10) // 2
  mod_dexterity = (dexterity - 10) // 2
  mod_constitution = (constitution - 10) // 2
  mod_intelligence = (intelligence - 10) // 2
  mod_wisdom = (wisdom - 10) // 2
  mod_charisma = (charisma - 10) // 2
  return mod_strength, mod_dexterity, mod_constitution, mod_intelligence, mod_wisdom, mod_charisma

mod_strength, mod_dexterity, mod_constitution, mod_intelligence, mod_wisdom, mod_charisma = get_ability_modifier(strength, dexterity, constitution, intelligence, wisdom, charisma)


print(f"new Strength: {mod_strength}")
print(f"new Dexterity: {mod_dexterity}")
print(f"new Constitution: {mod_constitution}")
print(f"new Intelligence: {mod_intelligence}")
print(f"new Wisdom: {mod_wisdom}")
print(f"new Charisma: {mod_charisma}\n")

print()

def treasure():
  treasure = random.randint(1,5)
  if treasure == 1:
    return "gold"
  elif treasure == 2:
    return "diamonds"
  elif treasure == 3:
    return "rubies"
  elif treasure == 4:
    return "emeralds"
  elif treasure == 5:
    return "sapphires"
    

def menu():
  action = input("Please choose from the following actions:\n 'attack' \n'negotiate' \n'search' \n'eat'\n")
  #attack
  if action == "attack":
    print("You're choosing to attack the enemy? Let's roll this 20-sided dice!")
    roll = random.randint(1, 20)
    print(f"You rolled a {roll}")
    print("Now, check your strength and dexterity, which would you like to use? (PRO-TIP: Choose the higher one!!)")
    strength_or_dexterity = input("'strength' or 'dexterity'? ")
    if strength_or_dexterity == "strength":
      hit_or_miss = roll + mod_strength
      print(f"You rolled a {roll} + {mod_strength} strenth = {hit_or_miss}")
      if hit_or_miss >= 12:
        print("You hit the enemy! Roll this six-sided dice to see how much damage you do!")
        damage = random.randint(1, 6)
        print(f"You did {damage} damage!")
      else:
        print("You missed the enemy!")
    if strength_or_dexterity == "dexterity":
      hit_or_miss = roll + mod_dexterity
      print(f"You rolled a {roll} + {mod_dexterity} dexterity = {hit_or_miss}")
      if hit_or_miss >= 12:
        print("You hit the enemy! Roll this six-sided dice to see how much damage you do!")
        damage = random.randint(1, 6)
        print(f"You did {damage} damage!")
      else:
        print("You missed the enemy!")
   
  #negotiate
  elif action == "negotiate":
    print("You're choosing to negotiate with the enemy? Let's roll this 20-sided dice to see how it goes for you!")
    nego_roll = random.randint(1, 20)
    print(f"You rolled a {nego_roll}!")
    nego_hit_or_miss = nego_roll + mod_charisma
    if nego_hit_or_miss >= 15:
      print("You negotiated a truce with the monster! He agreed to leave!")
    else:
      print("You failed to negotiate with the monster! He attacked you!")
  #search
  elif action == "search":
    print("You're choosing to search the area? Let's roll this 20-sided dice to see how it goes for you!")
    search_roll = random.randint(1, 20)
    print(f"You rolled a {search_roll}!")
    print("Now, check your intelligence and wisdom, which would you like to use? (PRO-TIP: Choose the higher one!!")
    intel_or_wisdom = input("'intelligence' or 'wisdom'? ")
    if intel_or_wisdom == "intelligence":
      search_hit_or_miss = search_roll + mod_intelligence
      print(f"You rolled a {search_roll} + {mod_intelligence} intelligence = {search_hit_or_miss}!")
      if search_hit_or_miss >= 12:
        print(f"congradulations! You found a treasure chest! There's {treasure()} inside!!!" ) 
      else:
          print("You failed to find anything!")
    if intel_or_wisdom == "wisdom":
      search_hit_or_miss = search_roll + mod_wisdom
      print(f"You rolled a {search_roll} + {mod_wisdom} wisdom = {search_hit_or_miss}!")
      if search_hit_or_miss >= 12:
        print(f"congradulations! You found a treasure chest! There's {treasure()} inside!!!" )
      else:
        print("You failed to find anything!")
            
  #eat
  elif action == "eat":
    print("The food in your purse is rancid! You're choosing to eat it? Let's roll this 20-sided dice to see how it goes for you")
    eat_roll = random.randint(1, 20)
    print(f"You rolled a {eat_roll}!")
    eat_hit_or_miss = eat_roll + mod_constitution
    if eat_hit_or_miss >= 10:
      print("You ate the food! It was bad, but you lived!")
    else:
      print("You ate the food! It was too rancid and you must stay in bed from the sickness!")
  else:
    print("Invalid action. Please choose again.")
  menu()
  

  return action

#Repeated four times
menu()
print("Let's do it again!")
menu()
print("Let's do it again!")
menu()
print("Let's do it again!")
menu()