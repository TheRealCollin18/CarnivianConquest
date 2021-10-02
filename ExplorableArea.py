from Merchant import Merchant
from textcolor import TextColor
from monsterlist import monsters
from items_list import Items_list
from HEALINGitems import Healingitems
class Area(): 
    name = ""
    story_item = ""
    minlevel = 0
    maxlevel = 0
    area_dungeon = "" #name?
    mob_list = []
    loot_pool = []
    area_boss = ""
    boss_loot = []
    #Boss_defeated = False 
    WSloot = [Items_list.SuspicousScale, Items_list.Mushroom, Healingitems.PurifiedSwampWater]
    WStext = ["Reeve Pierce walks around the swampy landscape and scouts out any signs of the Wallubine. He spots a suspicous looking fish scale near the edge of the river and picks it up. It glows with a cyan light. May be useful. Reeve Pierce stuffs it into his bag and moves on",
        "Reeve Pierce runs into a dense patch of grass. He rumages through when he unearths 3 hearty looking mushrooms.", 
        "ReevePierce stumbles into a ancient pool of water. You reach down to take a sip when he realizes it healed the wounds on his hand. Reeve Pierce then scoops up some purified water into his canister and moves on."]
    #ambiance_text = {
    depth = 0
    #Changes colour of text for that nice feeling. Depending on region. :)

    def __init__(self, n, minl, maxl, ad, ml, lp, ab, bl, dp,  ):
      self.name = n
      self.minlevel = minl
      self.maxlevel = maxl
      self.area_dungeon = ad

      self.loot_pool = lp
      self.area_boss = ab
      self.boss_loot = bl
      self.depth = dp
      self.mob_list = monsters.enemy_list_dict.get(ml)
      
      # for i in range(self.level * 10):

      # self.loot_pool = lp
      # self.area_boss = ab
      # self.boss_loot = bl

    

    #prints the description while you explore the area. May give clues to a puzzle or quest.
    #returns string of Area description....
    def explore_text(self, hero_area):
      return {
        "WS" : self.WStext 
      }.get(hero_area)
    #This function actualy gives you the item that you gain from exploring around the area 
    def explore_items(self, hero_area):
      return {
        "WS" : self.WSloot
      }.get(hero_area)
    # Area_Menu
    #prints the options avialable when inside a explorable Area
    #returns nothing
    def area_menu(self,hero_area, user, depth):
      print(user.FindAmbiance(),end="")
      print("----------------------------")
      print(self.name)
      print("----------------------------") 
      print(TextColor.white,end="")
      user.printHp()
      user.printMagik()
      # if depth > 0:
      #   print
      # else:

      print("What will Reeve Pierce do?")
      print("1) " + TextColor.cyan + "Explore around swamp"+ TextColor.white)
      print("2) " + TextColor.red + "Open Inventory" + TextColor.white)
      print("3) " + TextColor.green + "Talk to Merchant"+ TextColor.white)
      print("4) " + TextColor.blue + "Explore deeper into the " + self.area_dungeon+ 
      (" (Dungeon Level) " if depth == self.depth else 
      (" (Depth: "+str(depth)+ ")" if depth > 0 else " (Depth: Surface Level)")) ,
      TextColor.white)
      
    def ExploreAreaSequence(self, hero_area, user, contrl):
      invalid = False
      while invalid == False:
        self.area_menu()
      #TODO Create main gameplay loop for exploreable area


      #there will be a method to say enter the dungeon persay...
      ##in that we run textcolor = FindAbiance
      #print(textcolor+self.explore_text)
    


