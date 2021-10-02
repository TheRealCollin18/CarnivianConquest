from armory import armory
from weapons import Weapons
from items import Items
from textcolor import TextColor
from HEALINGitems import Healingitems
class Merchant():
  wsListOfItems = [armory.Broom, armory.BetrayalsSting, armory.WoodenSpear, Healingitems.SmallHealingPotion]
  introDia = ""
  GreetingDia = []
  items = {
      "WS": wsListOfItems,
  }
  advice = {
    "WS" : "Advice? Well I have plenty of advice to give, but I have a feeling you want to know about the Wallubine. Not much is known about it, but fish are attracted to their own scales. Hopefully that helps you on your journey. Good Day sir!"
  }
  intro_dict = {
    "WS" : "Hello young adventurer welcome to the Terford Shop! Care to paruse my wares?"
  }
  def MerchantTutorial(self, hero):
    input("Hello young adventurer! I am Wilfred, your guide, aid, and shopkeeper on your numerous explorations and battles. Oh and I do see that you have the general's sword on your back. For soildiers of Carnivia I give a special discount! Cant go stopping the Ravager without proper gear, now can you? ")
    input("Which leads me to tell you that as your opponents get stronger and stronger, i can provide even better gear. Isnt that neat?")
    input("To buy from me I use the very simple system of numbers. Each number correnspodes to a different item in my shop. Tell me the item and ill give it to you for the corrensponding price.")
    input("As a collecter of many wares I too can purchase any item that you procure on your journey.")
    input("To obtain said money, is no easy feat. You could either kill enemies you see for money or take up bounties from the townsfolk or me to get paid a labor fee.")
    input("If you ever feel lost or unsure of yourself, im always here to give you help and friendly advice. Happy travels, and I hope to see you here often")
  def printMenu(self,hero):
    #add in intro dialouge here
    print("----------------------------")
    print("MerchantShop")
    print("----------------------------")
    print(hero.FindAmbiance() + "What will Reeve Pierce do?" + TextColor.white)
    print("Gold : " ,hero.money)
    print("1)"+ TextColor.green + " Buy" + TextColor.white)
    print("2)" + TextColor.red + " Sell" + TextColor.white)
    print("3)"+ TextColor.blue + " Advice" + TextColor.white)
    print("<--- EXIT")
        # print(user.FindAmbiance() + "What will "+user.Name+" do?" + TextColor.yellow)

        #

  def sellMenu(self):
    print("What kind of item do you wish to sell?")
    print("1) Weapons")
    print("2) Items")
    print("<--- BACK")
    
  def Advice(self, hero):
    thing = self.advice.get(hero.area)
    print(thing)
  def sell(self, hero):
    while True:
      self.sellMenu()
      choice = input(": ")

      #first check is too make sure that Nothing was not entered...
      if choice == "":
        print("please enter SOMETHING")
        continue
      elif choice[0].upper() == "B":
        return False

      try:
        choice = int(choice)
      except:
        print("please enter a NUMBER")
        continue

      if choice == 1:
        self.sellWeapon(hero)
        break
      elif choice == 2:
        self.sellItem(hero)
        break
      
      else:
        print("please enter a NUMBER or BACK!!!")
      

  def buy(self,hero):
    #poruse as long as you like traveller
    while True:  
      self.displayItems(hero)
      print("<--- BACK")
      choice = input(": ")
      itemsList = self.items.get(hero.area)
      if choice[0].upper() == "B":
        break
      else:
        try:
          choice = int(choice)
        except:
          print("please enter a NUMBER or BACK!!!")
          continue
          
        if hero.money >= itemsList[choice- 1].price:
          #check on the item to see what type it is, if its a weapon 

          #type(item) --> Weapons or Items...
          if type(itemsList[choice- 1]) == Weapons:

            if hero.addToWeaponList(itemsList[choice-1]):
              hero.money -= itemsList[choice-1].price
              itemsList.remove(itemsList[choice-1])
              input("Thank you for your purchase!")
            else:
              input("Ah it seems you cannot fit another item my good adventurer perhaps I could relieve you of some of extra arms...")
          elif type(itemsList[choice-1]) == Items:
            if hero.addToInventory(itemsList[choice-1]):
              hero.money -= itemsList[choice-1].price
              itemsList.removeitemsList[choice-1]
              input("Thank you for your purchase")
            else:
              input("Oh I do see you do not have enough space in your inventory there. Care to upgrade?")
          else:
            #this is the case when the item chosen is a Healing Item...
            hero.givePotion(itemsList[choice-1])
            hero.money -= itemsList[choice-1].price
            input("Thank you for your purchase")
        else:
          input("It seems you have insufficient funds to purchase this item. I am sorry")
     

    #itemsList[y]
  #displaying all the inventory he has to offer in a nice way
  #all the items in order
  def displayItems(self, hero):
    #y starts at 0 and will till it ends
    itemsList = self.items.get(hero.area)
        
    for y in range(len(itemsList)):
      print(str(y+1)+": "+ itemsList[y].name + "  __" , itemsList[y].price, "__")
  #all the prices in order

  def addItem(self, itemToAdd, area):
    self.items.get(area).append(itemToAdd)
      
  def sellWeapon(self,hero):
    #first thing print out all weapons in weapon list on hero...
    count = 1
    for y in hero.weapon_list:
      print(count, ": ",y.name, "__" , y.sellPrice , "__")
      count += 1 
    print("<------ Back")
    while True:
      choice = input(": ")
      #checking if nothing is typed
      if choice == "":
        print("please enter a NUMBER!!!!")
        continue
      if choice[0].upper() == "B":
        return False
      else:
        choice = int(choice) #this can still cause a break, but its unlikely... ish
        check = input("Are you sure you want to sell this? \nY/N: ") 
        swpn = hero.weapon_list[choice-1]  
        if check[0].upper() == "Y":
          #print("accepted yes")
          
          if hero.removeWeapon(hero.weapon_list[choice-1]):
            hero.money += swpn.sellPrice
            self.addItem(swpn,hero.area)
            print("Thank you")
            break
          else:
            print(" traveller please submit a valid answer")
            continue
        else:
          break

    #check that choice isnt empty
    #check that choice is back,

    #choice --> number... we use that number to get the weapon from weapon_list... (weapon_list[choice]) --> is a weapon

    #give hero money before
    #as well as using the merchants add item
    

    #weapon_list.remove(weapon_list[choice])
    

  #example_list.add(example)
  def sellItem(self,hero,):
    hero.printInventory(True) #add the amount of the item to the print
    while True: 
      choice = input("Which item do you want to sell? ")
      if choice[0].upper() == "B":
        return False
      if choice == "":
        print("please enter a NUMBER!!!!")
        continue
      
      else:
        choice = int(choice)
        sitem = hero.inventory[choice-1]
        if sitem.story == True:
          print("No sir, I can't buy this item. Its too special to be sold in my market")
          
        else:
          amount = int(input("how many? "))
          check = input("Are you sure you want to sell this? Y/N")
          if check.upper()[0] == "Y":
            sitem.amount -= amount
            if sitem.amount == 0:
              hero.inventory.remove(sitem)
             #meake a new function for hero that removes the amount of items correctly
            hero.money += sitem.price * amount
            self.addItem(sitem,hero.area)
            print("Thank you!")
            print("Reeve Pierce has gained" , sitem.price , "gold!")
          if check.upper()[0] == "N":
            break
        break
        
    
  





#wallabineMerchant = Merchant()
#wallabineMerchant.addItem(Armory.weapon)  
