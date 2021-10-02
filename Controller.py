from character import Character
from SpellList import SpellList
from SupportMagik import SupportMagik
from HEALINGitems import Healingitems
from armory import armory
from textcolor import TextColor 
from monsterlist import monsters
from ExplorableArea import Area
from monsterlist import monsters
from sideeffects import SideEffects
from elements import Elements
from Merchant import Merchant
from ExplorableArea import Area
from AreaList import AreaList
from items import Items
#Collin Was Here
import random
#This class controls everything that happens in the game
class Controller():
    SupMagik = SupportMagik()
    ReevePierce = Character()
    merchant = Merchant()
    def InventorySelection():
      print("Which inventory slot do you want to open?")
      print("1) Weapons")
      print("2) HealingItems")
      print("3) Items")
    #Weapons
    def FindAttackSpell(self, user, enemy, choice):
        self.heldAttackSpell = SpellList.spells[choice]
        print(self.heldAttackSpell)

    #Confirms Yes or No input
    #return True if yes, False for if no
    def ConfScrn():
        print("CONFIRM     ")
        ans = input("(Y/N): ")
        ans = ans.upper()[0]
        while not ans == "Y" and not ans == "N":
            print("    ERROR, PLEASE TRY AGAIN    ")
            print("   CONFIRM     ")
            ans = input("(Y/N): ")
            ans = ans.upper()[0]
        return ans=="Y"

    #prints the menu for attack magik spells
    def AMM(self,user,enemy):
            canCast = user.printAttackSpellsMenu()
            if canCast:
                choice  = input(": ")
                #do not allow user to choose options that are unavailable
                ####
                #"B" "b"
                choice[0].upper() #this takes the uppercase of the frist character of choice
                choice.upper()[0] #takes the first character of the uppercase version of choice
                while len(choice) == 0:
                  print("invalid choice")
                  print("try again")
                  user.printAttackSpellsMenu()
                  choice = input(": ")
                if not choice[0].upper() == "B":
                    canCast = user.CastAttackSpell(int(choice) - 1, enemy)
                    while not canCast:
                        print("Not enough Magik to cast spell "+user.attack_spells[int(choice)-1].NameoSpell+", please choose another spell")
                        print("----------------------------------------")
                        user.printAttackSpellsMenu()
                        choice = input(": ")
                        canCast = user.CastAttackSpell(int(choice) - 1, enemy)
                else:
                    canCast = False
            else:
              print("No Attack Spells can be CAST!")
            return canCast

    #Changed invalid to valid
    #returns False instad of True if used a spell
    def SMM(self,user, enemy):
        print("----------------------------------------")
        canCast = user.printSupportSpellsMenu()
        if canCast:
            choice = input(": ")
            

            if not choice.upper()[0] == "B":
                #inside this CastSupportSpell is where we need to put the major logic for running a spell
                user.CastSupportSpell(choice,self.SupMagik, enemy)
        return canCast
                
    #return true if the target can still use a move
    def check_side_effect(self,target):
      #this is for burn, paralyzed, frozen, and poisoned...
      #target has a attribute.side_effect that we can check directly to see...
      #Frozen and Paraly
      if target.side_effect ==  None:
        return True 
      else: 
        if target.side_effect_dur > 0:
          if target.side_effect == SideEffects.Paralyzed:
            print(target.Name+" is "+TextColor.yellow+"Paralyzed "+TextColor.white+" and cannot make a move!")
            return False
          elif target.side_effect == SideEffects.Freezed:
            print(target.Name+" is "+TextColor.blue+"Frozen"+TextColor.white+" and cannot make a move!")
            return False
          elif target.side_effect == SideEffects.Burn:
            losthp = int(target.Max_hp *.1)
            target.hp -= losthp
            print(target.Name+" has lost"+TextColor.red,losthp,TextColor.white+" from "+TextColor.orange+"its Burn!"+TextColor.white)
            return True
          elif target.side_effect == SideEffects.Poison:
            losthp = int(target.Max_hp *.05)
            target.hp -= losthp
            print(target.Name+" has lost"+TextColor.red,losthp,TextColor.white+" from "+TextColor.brightgreen+"Poison!"+TextColor.white)
            return True
          elif target.side_effect == SideEffects.Blinded:
            cannotattack = random.randint(1,2)
            if cannotattack == 1:
              return True
            else:
              print(target.Name + " Is completely " + TextColor.black + "blinded " + TextColor.white + "and has missed its attack")
              return False
          elif target.side_effect == SideEffects.Blessed:
            print(target.Name+" Is teaming with " + TextColor.magenta + "Blessed " + TextColor.white + "energy!")
            target.side_effect_dur -= 1
        else:
          if target.side_effect == SideEffects.Freezed:
            print(target.Name+" is no longer FROZEN!!!!")
          elif target.side_effect == SideEffects.Blessed:
            print(target.Name+" is no longer Blessed, Power returns to normal")
            target.Power-= 6
          target.side_effect = None
          
          return True
          
        
    #function prints basic options for battle
    #return nothing
    def printFightMenu(self,user):
        print(user.FindAmbiance() + "What will "+user.Name+" do?" + TextColor.yellow)
        user.printHp()
        user.printMagik()
        print("1)"+ TextColor.red + " Attack" + TextColor.white)
        print("2)" + TextColor.green + " Heal" + TextColor.white)
        print("3)"+ TextColor.blue + " Spell" + TextColor.white)
        print("4) " + TextColor.cyan + "Swap Weapon" + TextColor.white)
        

    #prints the option of choosing either to use attack or support Spells
    #take in input and run AMM or SMM
    #returns Valid (true or false) 
    # only code that uses valid. its special :].
    def MagikMenu(self,user, enemy):
        valid = False
        
        while not valid:
            
            print("----------------------------------------")
            print(user.FindAmbiance() , "Which Spell Type?" + TextColor.white)
            print("1) " + TextColor.red + "Attack" + TextColor.white)
            print("2) " + TextColor.blue + "Support" + TextColor.white)
            print("3) BACK <--")
            choice = input(": ")
            choice = choice.lower()
            if choice == "1":
                valid = self.AMM(user, enemy)
            elif choice == "2":
                valid = self.SMM(user,enemy)
            elif choice == "3" or choice == "back":
                return False
            else:
                print("Invalid choice")
                valid = False
        return valid


    #prints
    #return if user is alive
    def fightSequence(self,user, enemy):
        TurnTracker = 0
        #this tracks the turn time for some of the multi-turn support spells
        print(user.Name +" was confronted by a(an) "+ enemy.ambiance + enemy.Name + "!" + TextColor.white)
        #To check if the fight sequence continues 
        while not user.isDead() and not enemy.isDead():
            #To show that you can continue with the code 
            #var to catch a invalid action by user.... redo loop
            invalid = False
            #if held_move is empty normal else--> line: 145
            if self.check_side_effect(user):

              if user.held_move == None:
                  #self.check_side_effect()
                  self.printFightMenu(user)
                  choice  = input(": ")
                  if  choice == "3":
                      #Shift this into its own function, then
                      #create a while loop to reprompt menu
                      if user.Magik <= 0:
                          print(user.Name + ("has no magik left to cast any spells!"))
                          invalid = True
                      else:
                          #MM returns valid, flip for invalid
                          invalid = not self.MagikMenu(user, enemy)
                      #self.FindAttackSpell()
                      #run the MagikMenu
                  elif choice == "2":
                      print("")
                      if Controller.ConfScrn():
                          user.Heal()
                      else:
                          invalid = True
                  elif choice == "1":
                      print("")
                      if Controller.ConfScrn():
                          user.Attack(enemy)
                      else:
                          invalid = True
                  elif choice == "4":
                    print("")
                    if Controller.ConfScrn(): 
                      if user.printWeaponsList():
                        user.swapWeapon()
                      else:
                        print("You have no weapons to swap to...")
                        invalid = True
                    else:
                      invalid = True
                    print("--------------------------------------------")
                    continue     
                  else:
                      print("")
                      print("Invalid action")
                      invalid = True

                  user.time_left -= 1 
                  if user.time_left == 0:
                      #the debuff spell function is store within the SupportMagik class,
                      # SupportMagik.debuffspell or what not....
                      SupportMagik.debuff_spell(user)
                      
                    
                    
              else: #use the held move
                  user.held_move(user,enemy)
              #These statements give Reeve Pierce expeirience 
            if not user.isDead() and not enemy.isDead() and not invalid:
              if self.check_side_effect(enemy):
                enemy.EnemyMove(user)
                print("----------------------------------------")
                TurnTracker += 1
                invalid = False
            if user.side_effect_dur >=0:
              user.side_effect_dur -= 1
        if not user.isDead():
            HWExp = enemy.expyield + random.randrange(-1, 3)
            user.exp += (HWExp)
            print("ReevePierce glowed with the fallen " + enemy.Name + "'s expeirience and gained" ,HWExp, "exp!")
            if user.exp >= user.maxexp:
                user.levelup()
        #reset all who need to be reset
        enemy.reset(enemy)
        
        return not user.isDead()
            #we already do a lot of printing within the functions themselves for return to sender, heavens blessing, etc. Here we just want to run it. Handle the logic here, do the other stuff in their respective classes

            #which we do. Let it be easy when you already did the hard part for yourself

            # if user.heldmove == self.ReturntoSender2:
            #   SupportMagik.ReturntoSender()
              
 
    def OSW(enemy):
      DNC = 0
      while True:
        if DNC == 0:
          input("The sun shines brightly on Reeve Pierces face. \n Options:\n 1) Look around \n 2) Further explore cave\n 3) Visit Traveling Merchant\n: ")
        DNC += 1

    
    # def DemofightSequence(self,user, enemy):
    #     TurnTracker = 0
    #     print(user.Name +" was confronted by a(an) " + enemy.name + "!")
    #     while not user.isDead() and not enemy.isDead():
    #         invalid = False
    #         #if user.hp < 5 and enemy.Name == "Earthborn":
    #           #print("Reeve Pierce's hands suddenly glowed green and blasted hundreds thorns and brambles that tangled and choked the Earthborn to death.")
    #           #enemy.isDead
    #         self.printFightMenu(user)
    #         choice  = input(": ")
    #         if  choice == "3":
    #             #Shift this into its own function, then
    #             #create a while loop to reprompt menu
    #             if user.Magik <= 0:
    #               print(user.Name + ("has no magik left to cast any spells!"))
    #               invalid = True
    #             else:
    #               self.AMM(user, enemy)
    #             #self.FindAttackSpell()
    #             #run the MagikMenu
    #         elif choice == "2":
    #             print("")
    #             user.Heal()
    #         elif choice == "1":
    #             print("")
    #             user.Attack(enemy)
    #         else:
    #             print("")
    #             print("Invalid action")
    #             invalid = True
    #         if not user.isDead() and not enemy.isDead() and not invalid:
    #             enemy.EnemyMove(user)
    #         print("----------------------------------------")
    #         TurnTracker += 1
    #         invalid = False
    #     if not user.isDead():
    #         HWExp = enemy.expyield + random.randrange(-2, 3)
    #         user.exp += (HWExp)
    #         print("ReevePierce glowed with the fallen " + enemy.name + "'s expeirience and gained" ,HWExp, "exp!")
    #         if user.exp >= user.maxexp:
    #             user.levelup()
    #         return True
    #     else:
    #         return False
    #     TurnTracker = 0
    

    def battle1(self):
        for i in range(4):
          self.ReevePierce.levelup()
        #sudo main
        #self.ReevePierce.addAttackSpell(spells[])
        
        self.ReevePierce.addToWeaponList(armory.MagmaFists)
        self.ReevePierce.addToWeaponList(armory.SoldiersBow)
        self.ReevePierce.addToWeaponList(armory.Reganae)
        self.ReevePierce.givePotion(Healingitems.MediumHealingPotion)
        self.ReevePierce.givePotion(Healingitems.SmallHealingPotion)
        self.ReevePierce.attack_spells = SpellList.attack_spells
        self.ReevePierce.support_spells = SpellList.support_spells

        

        # SideEffects.apply_side_effect(Elements.Ice, self.ReevePierce,"defending")

        
    #def CaveEncounter(self):
     # return self.fightSequence(self.ReevePierce,monsters.)

    # def battle2(self):
    #     #add in the stuff for the next conflict
    #     return self.DemofightSequence(self.ReevePierce,monsters.BearDeer)

    def merchant_sequence(self):

      

      #print out the merchant intro
      input(self.merchant.intro_dict.get(self.ReevePierce.area))
      #lets print out the merchant menu...

      while True:
          self.merchant.printMenu(self.ReevePierce)
          choice  = input(": ")
          if choice == "1":
            self.merchant.buy(self.ReevePierce) 
          elif choice == "2":
            self.merchant.sell(self.ReevePierce)
          elif choice == "3":
            self.merchant.Advice(self.ReevePierce)
          elif choice == "":
            print("I'm afraid I don't understand what you just asked could you repeat that?")
            continue
          elif choice[0].upper() == "E":
            break
          else:
            print("I'm afraid I don't understand what you just asked could you repeat that?")
          print("------------------------------------")
    

    def EAS(self):
      tracker = 0
      area = AreaList.AreaFinder.get(self.ReevePierce.area)

      
      # self.ReevePierce.givePotion(Healingitems.MediumHealingPotion)
      self.ReevePierce.givePotion(Healingitems.SmallHealingPotion)
      # self.ReevePierce.attack_spells = SpellList.attack_spells
      # self.ReevePierce.support_spells = SpellList.support_spells
      while True:
        
        area.area_menu("cave", self.ReevePierce, tracker)
        choice = input(": ")
        if choice == "1":
          tracker = 0
          explore = area.explore_text(self.ReevePierce.area)
          explItem = area.explore_items(self.ReevePierce.area)
          if len(explore) == 0 :
            input("Reeve Pierce has explored all of the area around " + area.name )
          else:
            
            #placeholder1 = "3"
            randomness = random.randint(0, len(explore)-1 )
            input(explore[randomness])
            input("Reeve Pierce has gained " + str(explItem[randomness].amount) + " " +  explItem[randomness].name)
            self.ReevePierce.loot(explItem[randomness])
            #This removes the item and explore text so that we dont do it again 
            explore.remove(explore[randomness])
            explItem.remove(explItem[randomness])


    #uh oh the man has lagged out again







        elif choice == "2":
          while True:
            Controller.InventorySelection()
            choice = input(": ")
            if choice == "1":
              pass#weapons 
              if self.ReevePierce.printWeaponsList():
                self.ReevePierce.swapWeapon()
              else:
                print("You have no weapons to swap to...")
              break
            elif choice == "2":
              self.ReevePierce.Heal()
              break
            elif choice == "3":
            

              if self.ReevePierce.printInventory(False):
                choice = input(": ")
                if choice[0].upper() == "B":
                  break
                #Check to see if the user is at the dungeon
                #check to see if choice is less than the len of
                else:
                  choiceint = int(choice)
                  if choiceint > len(self.ReevePierce.inventory):
                    print("Choose another item")
                  else:
                    if self.ReevePierce.inventory[choiceint-1].story == False:
                      self.ReevePierce.simpleprint(choiceint-1)
                    else:
                      if tracker == area.depth:
                        print(Items.story_dict.get(self.ReevePierce.inventory[choiceint-1].name))
                        #activate boss fight...
                        enemy = monsters.Wallubine
                        # level within the areas min and max level
                                  
                        # print(enemy.Name)
                        # print(enemy.level)
          
                        return self.fightSequence(self.ReevePierce,enemy)
                        
                      else:
                        print("You can not use this item here")
                    
                break
            else:
              print("Please choose a option from the menu")



        elif choice == "3": 
          tracker = 0
          self.merchant_sequence()
        elif choice == "4":
          tracker += 1 
          
          #we want to generate a enemy to fight at random, based on the area the user is in...
          # random.choice(some_list) --> a random element from some_list
          enemy = random.choice(area.mob_list)
          randomness = random.randint(area.minlevel,area.maxlevel)
          enemy.set_level(randomness)
          #scale the level of the enemy to a random level within the areas min and max level
          #area
          print(enemy.Name)
          print(enemy.level)
          
           #now that our enemy is properly scaled, we can then initiated the fightsequence

          #fightSequence returns true or false, depending on if reeve pierce is alive...
          if self.fightSequence(self.ReevePierce,enemy) == True:
            #create a chance to loot
            pass
          else:
            #THE PLAYER HAS PERISHED
            break
            print("Type in a number")
        else:
          print("Please enter a option from the menu")


          #self.battle1()


      
      print("")