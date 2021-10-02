from enemies import Enemies
from armory import armory
from elements import Elements
from textcolor import TextColor
#Different monsters that can be spawned througout the game, with their own respective areas
class monsters():
  
  #def __init__(self, hp, w, n, armr, ele, lvl, maxhp, ex, hm, mk, am, te, po)
  StoneCentipede = Enemies(10, armory.Teeth, "StoneCentipede", 3, Elements.Earth, 1, 10, 4, False, 0, 0, TextColor.black, None, 0,)

  MountainGnome = Enemies(14, armory.WoodenSpear, "MountainGnome", 3, Elements.Earth, 1, 14, 4, False, 0, 0, TextColor.yellow, None, 0)

  DirtGolem = Enemies(13, armory.GolemFists, "Golem", 1, Elements.Earth, 1, 13, 6, False,0,0, TextColor.yellow, None, 0,)

  Earthborn = Enemies(11, armory.Teeth, "Earthborn", 0, Elements.Earth, 1, 11, 4, False,0, 0, TextColor.yellow, None, 0)

  Wolfbear = Enemies(23, armory.Claw, "Wolfbear", 1, Elements.Forest, 1, 23, 14, False,0,0,  TextColor.green,  None, 0)

  Lich = Enemies(15,armory.Sythe,"Lich", 0, Elements.Dark, 1, 15, 30,True, 7,7,TextColor.black,None, 0)

  Bat = Enemies(9, armory.Teeth, "Bat", 0, Elements.Toxic, 1, 9, 3, False, 0,0, TextColor.magenta, None, 0)

#boss |
#    \ /
#Pro tip: only bosses have two elements
  Wallubine = Enemies(42, armory.ElectricFins, "Wallubine", 0, Elements.Electric, 5, 23, 14, False,0,0, TextColor.blue, Elements.Water, 2)
  
  MountainMonsters_List = [MountainGnome, DirtGolem, Earthborn, Wolfbear]

  ForestMonsters_List = []

  CaveMonsters_List = [Earthborn, DirtGolem, Bat, StoneCentipede]

  RuinMonsters_List = []

  AllMonsters = []

  enemy_list_dict = {
      "cave" : CaveMonsters_List,
      "forest" : 2,
      "mountain" : MountainMonsters_List,
      "ruin" : 4, 
      "all" : 5
  }

  #Centamoth = Enemies(8, armory.)

