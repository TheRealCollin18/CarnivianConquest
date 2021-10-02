from main import Wallubine_Swamp
from ExplorableArea import Area 
from monsterlist import monsters
class AreaList():
  #self, n, l, ad, ml, lp, ab, bl, depth
  WallubineSwamp = Area("WallubineSwamp", 2,4, "LiersCave", "cave", [], monsters.Wallubine,[], 5)
  AreaFinder = {
    "WS", Wallubine_Swamp
  }