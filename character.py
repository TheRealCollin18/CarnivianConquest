import random
from weapons import Weapons
from AttackMagik import AttackMagik
from elements import Elements
from SupportMagik import SupportMagik
from HEALING import Healing
from textcolor import TextColor
from sideeffects import SideEffects
from items_list import Items_list
from items import Items
from armory import armory 

#Class definition for the main character in our game
class Character:
    Name = "Reeve Pierce"
    hp = 20
    Max_hp = 20
    #Max_hp = hp #<----Dis basically dis -----> 10/10
    exp = 0
    #Allows ReevePierce to learn more spells and become stronger
    maxexp = 10
    #The goal that, when achieved, makes ReevePierce grow a level
    inventory = [Items_list.SuspicousScale, Items_list.FossilizedDung] #two seperate things
    max_inventory = 15
    weapon_list = [] #two seperate things
    max_weapons = 4
    Armor = 0 #
    backround = "Poor Civilian in Raddish Town"#debunked 
    money = 1500 #Gold Tokens used in buying weopens, potions, and other special items
    skill = "Mage" 
    #The main skill set for ReevePierce
    Max_Magik = 10
    #The Max Magik that ReevePeirce can have
    Magik = 10
    #base element type
    element = Elements.Normal
    #Required to cast spells
    attack_spells = []
    #support spells are stored as their string counter parts
    #supMagik = SupportMagik()
    support_spells = []
    weapon = armory.SoldiersSword
    #The main factor in the damage output of ReevePierce
    time_left = 0
    level = 1
    Power = 2
    Potions = [] #RIP POTIONS JK Ex. [basic_potion, ect]
    held_move = None #holds a move to be used in the next turn....
    side_effect = None
    #WS - Wallubine Swap
    area = "WS"
    DFE = 0 #Enemies full damage
    side_effect_dur = 0

    
    #Moves:
    def Heal(self):
      canUse = self.HM()
      if not canUse:
        print("You are out of restoring item!!!!")
      else:
        
        which1 = input(": ")
        if which1.lower()[0] == "b":
          return False
        else:
          while int(which1) > len(self.Potions):
            print("Not a option you can choose from!")
            which1 = input(": ")
          which1 = int(which1)
          #which1 will be a number from 1 - len(self.Potions) so we have to reduce this number by 1 to use it with out Potions list
          
          self.Potions[which1-1].use(self)
          return True
          #function is ambiguous 
        

          #See what poitions you have available, i.e. which of the potions in the list do not have amount = 0
          #NEED HEALING MENU --> reference printAttackSpellsMenu to see idea of...

          #return false if the heal doesn't work for any reason...

          #Old code
          #

          #if at max hp, print that we are already full
          #if self.hp == self.Max_hp:
          #    print(self.Name+" is already at max Health!")
          #elif self.Potions > 0: #check to see if we have potions
          #  self.Potions -= 1
          #  amount = int(self.Max_hp / 3)
          #  if self.hp + amount > self.Max_hp: #dont heal over max
          #    amount = self.Max_hp - self.hp
          #  self.hp += amount
          #  print(self.Name+" used a potion")
          #  print(self.Name+" recovered",amount,"hp")
          #else:
          #  print(self.Name+"'s potion reserves are empty!")
        
    def HM(self):
      havePrinted = False
      tracker = 1
      for f in self.Potions: #an advanced for loop...
      #each iteration makes the variable 'f' equal to the object inside the loop.        print(f.amount)
        if not f.amount <= 0:
          havePrinted = True
          if f.Magiks > 0 and f.Heals <= 0:
            print(tracker, ") " + f.Name + " : refreshes" , f.Magiks, "Magik : " , f.amount, "potions left")
          elif f.Heals > 0 and f.Magiks <= 0:
            print(tracker, " : " + f.name + " : Heals" , f.Heals, "Health : " , f.amount, "potions left")
        tracker +=1
      if havePrinted:
        print("<-- BACK")
      return havePrinted  #to see if there is any healing items to use!

    
    # def AttackString(self, Enemy):
    #   DamageInAll = self.weapon.damage + self.Power + random.randint(-1,1)
    #   self.weapon.getSaying(self.name,Enemy.name,DamageInAll)
      
    
    def Attack(self, Enemy):#ReevePierce.Attack(NewEnemie)
        #update later
        #self.weapon.damage is set in stone. so lets say 7
        #this will lower the durability of the weapon
        #The total amount of damage dealt to an enemy
        #The Power of ReevePierce is added to the damage output
        #randomness added just to add that tiny hint of uncertainty when attacking where as spells are completely reliable in damage output
        elementBonus = Elements.TypeMachups(self.weapon.element, Enemy.element)

        DamageInAll = (self.weapon.damage + self.Power/2) * elementBonus + random.randint(-1,1)
        
        self.weapon.use()
        # print(self.Name + " uses his " + self.weapon.nameofweapon + " to attack " + Enemy.name)
        print(self.weapon.getSaying(self.Name,Enemy.Name,str(DamageInAll - Enemy.armor)))
        #check if element bonus is >1 2* or 4* or if it is <1
        if elementBonus < 1:
          print(TextColor.orange+"It was Not Very Effective...", TextColor.white)
        elif elementBonus > 1:
          if elementBonus == 2:
            print(TextColor.brightgreen+"It was Super Effective", TextColor.white)
          elif elementBonus == 4:
            print(TextColor.brightgreen+"It was EXTREMELY EFFECTIVE!!")
        elif elementBonus == 0:
          print("It had no effect!")

        
        Enemy.TDE( DamageInAll )

    def printWeaponsList(self):
      tracker = 0
      print("Current weapon:", self.weapon.name, "," , self.weapon.damage , "damage\n")
      for z in self.weapon_list:
        tracker += 1 
        print(tracker,": " + z.name + " , " + z.element.toString() + " ," , z.damage , "damage")
      print("<-------- BACK")
      return tracker != 0

    def swapWeapon(self):
      choice = input(": ")
      if choice[0].upper() == "B":
        return False
      choiceint = int(choice)
      choice2 = self.weapon_list[choiceint-1]
      self.weapon_list[choiceint-1] = self.weapon 
      self.equipWeapon(choice2)
      print("You have switched your current weapon " + "with " +
       self.weapon.name)
      

    def removeWeapon(self, choice):
      #return the weapon that is removed...
      try:
        self.weapon_list.remove(choice) #can fail if what is given does not exist....
        print("You have removed your " + choice.name + " from your inventory.")
        return True
      except:
        print("invaild option for removing weapon...")
        return False

    def removeItem(self, choice):
      try:
        self.inventory.remove(choice)
        print("You have removed your " + choice.name + " from your inventory. ")
        return True
      except:
        print("Invaild option for removing an item")
        return False


    #def Swap_Weapon(self):
      
        
    
    def CastAttackSpell(self, whichSpell, enemy):
        try:
            if self.Magik < self.attack_spells[whichSpell].Magik:
                return False

            print(self.Name + " chants "+ self.attack_spells[whichSpell].MagikSaying + "!!!")
            DamageInAll = self.attack_spells[whichSpell].Damage * Elements.TypeMachups(self.attack_spells[whichSpell].Element, enemy.element)

            print("ZAP! " + self.Name + " casts " + self.attack_spells[whichSpell].NameoSpell + " and dealed", DamageInAll  ,"to " + enemy.Name + "!") 

            #This prints if it is supereffective or not
            if   Elements.TypeMachups(self.attack_spells[whichSpell].Element, enemy.element) < 1:
              print(TextColor.orange+"It was Not Very Effective...", TextColor.white)
            elif Elements.TypeMachups(self.attack_spells[whichSpell].Element, enemy.element) > 1:
              if Elements.TypeMachups(self.attack_spells[whichSpell].Element, enemy.element) == 2:
                print(TextColor.brightgreen+"It was Super Effective", TextColor.white)
              elif Elements.TypeMachups(self.attack_spells[whichSpell].Element, enemy.element) == 4:
                print(TextColor.brightgreen+"It was EXTREMELY EFFECTIVE!!")
            
            #see if spell applys buff to hero
            SideEffects.apply_side_effect(self.attack_spells[whichSpell].Element, self,"attacking")

            #apply the side effect...
            SideEffects.apply_side_effect(self.attack_spells[whichSpell].Element, enemy,"defending")

            #self.attack_spells[whichSpell].Damage
            self.Magik -= self.attack_spells[whichSpell].Magik
            enemy.TDE(DamageInAll)
            #a check to see if ReevePierce has any Magik left to use spells
            if self.Magik == 0:
                print("No Magik left on Reeve Pierce!")
                return True
            else:
                print(self.Magik, "/", self.Max_Magik, "Magik Left on ReevePierce")
                return True
        except Exception as e:
            print(e)
            print("Incorrect option for spell")
            return False
        
  
    def CastSupportSpell(self, choice, sup_Magik, enemy): #self is the character, and reeve pierce does not have the support magik dict 

        #here we check to see if the spell can be cast, then do it if it can
        if SupportMagik.sup_magik_cost_dict.get(int(choice))(self) <= self.Magik:
            
            # if (spell is return to sender)
            #     user.heldMove = self.ReturnToSender2


            #things to keep in mind here. First: all support spells are methods attached to the sup magik Class. Second: the support spells are just a list of names inside the character. Lastly, if we want to do anything with the functions we have to do so in accordance with the above.


            #execute the spell. this should work better?
            print(SupportMagik.sup_magik_dict.get(choice)(sup_Magik,self,enemy))#I need to finish Return to sender
            self.Magik -= SupportMagik.sup_magik_cost_dict.get(int(choice))(self)
            #I did a change here but it doesn't seem to have worked
        else:
            print("Not Magik left on Reeve Pierce!")

    #user.printSpellMenu(user.attack_spells or user.support_spells)
    
    def printInventory(self, check):
      
        if len(self.inventory) != 0: 
          if check == False:
            print("Which item do you want to use?")
        else:
          print("No items in inventory")
          return False
        tracker = 0
        
        for z in self.inventory:
          
          print(tracker+1, " : " , z.name, " - ", z.amount)
          
          tracker += 1
        print("<------ BACK")
        return True
        
      
        
    def simpleprint(self, choice):
      #choice will be scaled to work with inventory
      
      # check to make sure the choice is within the bounds of the inventory (i.e. less than its len)


      TheItem = self.inventory[choice]
      print("Name = ",TheItem.name)
      print("Amount = ",TheItem.amount)
      print("Sell price = $", TheItem.price)
      
        
      

    #helperMethods 
    def printAttackSpellsMenu(self):
        #here we will go through the spells available, and only print and give the option for the ones we have enough magik to use
       
        #put the stuff before here*******
        #do you want to say the Element? or power either or
        #create a variable to see if we printed
        havePrinted = False
        for i in range(len(self.attack_spells)):
            if self.attack_spells[i].Magik <= self.Magik:
                print(i+1,':',self.attack_spells[i].NameoSpell)
                havePrinted = True
                #1 (15,asdf,aoeuaoeu,12)             i: 0
                #2 ghjk             i: 1
                #3 k';l             i: 2
        if havePrinted == True:
            print("<--- BACK")
        return havePrinted

    def printSupportSpellsMenu(self):
        #print(self.support_spells)
        havePrinted = False
        #support spells is a list of names of support spells available to the character.

        #check to see if the user's time_left value is equal to 0 or lessthan , if not then you cannot use support magik...
        if self.time_left > 0:
          print("You can only cast one support spell at a time!")
        else:
        #support_spells = ["ReturnToSender","FullShield"]
          for i in range(len(self.support_spells)):
            #put the function that calculates the cost of each spell into costAmount
            # costAmount = SupportMagik.sup_magik_cost_dict.get(self.support_spells[i]) 
            #calc cost for current spell
            if SupportMagik.sup_magik_cost_dict.get(i+1)(self) <= self.Magik: #if spell at index i in support_spells magik is > the characters magik do not print
                print(i+1,':',self.support_spells[i])
                havePrinted = True

        if havePrinted:
            print("<--- BACK")
        return havePrinted

    #troubleshooting functions
    def printHp(self):
        print("Current HP:",self.hp, "/", self.Max_hp)
        
    def getMoney(self):
        return self.money

    def printExp(self):
      print(self.exp)
    
    def isDead(self):
      return self.hp <= 0
    
    def printWeapon(self):
      print(self.weapon)

    
    def takeDamage(self, damageInflicted ):
      HealthBefore = self.hp
      self.hp -= damageInflicted - self.Armor
      if self.isDead(): #check to see if user died
          print(self.Name+" has perished....")
      if self.hp > HealthBefore: #check to see if user healed from damage
        print(self.Name, "'s armor repelled the damage")
        self.hp = HealthBefore 
      self.DFE = damageInflicted - self.Armor  
     

    def printMagik(self):
      print("Current Magik:",self.Magik, "/", self.Max_Magik, TextColor.white)
    #Changes to character |
    #                     |
    #                     |
    #                    \ /
    #                     V
    def levelup(self):
      #This just increases all Reeve Pierce's stats. May have to balance this out later.
        randhp = random.randrange(2, 4) * self.level
        randmk = random.randrange(1, 2) * self.level
        self.Power += 2
        self.maxexp += random.randrange(6, 9)
        self.exp =- self.maxexp
        self.Max_hp += randhp
        self.Max_Magik += randmk
        self.hp += randhp
        self.Magik += randmk
        self.level += 1
        print(self.Name + " is now Level#"
         ,self.level , "!")
        print("Health",self.hp,"/",self.Max_hp)
        print("Magik",self.Magik,"/",self.Max_Magik)
        print("Power: ", self.Power)
    #Functions to help give spells and weapons and Potions to Reeve Pierce
    def equipWeapon(self, NewWeapon):
      self.weapon = NewWeapon

    def addToWeaponList(self, NewWeapon):
      #check to see if the len of weapons is at max, if not add weapon to weapons list and return true, otherwise return false
      if len(self.weapon_list) >= self.max_weapons:
        return False
      else:
        self.weapon_list.append(NewWeapon)
        return True
    
    def addToInventory(self, item):
      if len(self.inventory) >= self.max_inventory:
        return False
      else:
        self.inventory.append(item)
        return True

    def givePotion(self, NewPotion ):
      if NewPotion in self.Potions:
        #find where the Potion in self.Potions is
        #lets create a for loop and go until we find where NewPotion equals some item in the list...
        for z in self.Potions:
          #z will be a potion within self.Potions
          #so lets check if z is equal to NewPotion
          if z == NewPotion:
            z.amount += NewPotion.amount
            break
      else:
        #here we add the newPotion to the list of self.Potions
        self.Potions.append(NewPotion)
          

    def addItem(self, item):
      if item in self.inventory:
        #find where the Potion in self.Potions is
        #lets create a for loop and go until we find where NewPotion equals some item in the list...
        for z in self.inventory:
          #z will be a potion within self.Potions
          #so lets check if z is equal to NewPotion
          if z == item:
            z.amount += item.amount
            break
      else:
        #here we add the newPotion to the list of self.Potions
        self.inventory.append(item)

      
      print(item.name+" has been added to your inventory")

    def addAttackSpell(self, newSpell):
        self.attack_spells.append(newSpell)
    
    def addSupportSpell(self, newSpell):
        self.support_spells.append(newSpell)
        
    def FindAmbiance(self):
      return {
        "WS" : TextColor.brightgreen
      }.get(self.area)

    def loot(self, item):
      do = {
        Healing: self.givePotion,
        Items: self.addItem,
      }.get(type(item))
      do(item)
       