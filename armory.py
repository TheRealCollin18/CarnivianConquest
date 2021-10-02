from weapons import Weapons
from elements import Elements

#NameofWeapon = Weapons(Durability, Damage, Element, typeofweapon, nameofweapon)
class armory():
    WoodenSpear = Weapons(12, 2, Elements.Normal, "spear", "WoodenSpear", 10, 7)
    Reganae = Weapons(30, 11, Elements.Electric, "bow", "Reganae" , 50, 35)
    FishingSpear = Weapons(15, 7, Elements.Normal, "spear", "FishingSpear", 30, 21)
    GolemFists = Weapons(-1, 1, Elements.Earth, "fists", "GolemFists",-1,-1)
    MagmaFists = Weapons(-1, 13, Elements.Fire, "fists", "MagmaFists", -1, -1)
    Broom = Weapons(6, 3, Elements.Normal, "none", "Broom", 5, 3)
    TribalHammer = Weapons(25, 8, Elements.Forest, "hammer", "TribalHammer", 25, 17)
    Sythe = Weapons(13, 13, Elements.Normal, "sythe", "sythe", 30, 21)
    Fists = Weapons(-1, 1, Elements.Normal, "fists", "fists", -1, -1)
    IcicleSword = Weapons(21, 9, Elements.Ice, "sword", "IcicleSword", -1, 70)
    Claw = Weapons(-1, 5, Elements.Normal, "claw", "Claws", -1, 1)
    KingsHalberd = Weapons(59, 11, Elements.Normal, "spear", "KingsHalberd", 150, 105)
    BetrayalsSting = Weapons(22, 13, Elements.Dark, "bow", "Betrayals Sting", 10, 10)  #ShadowBow
    Downfall = Weapons(14, 16, Elements.Forest, "sythe", "Downfall", 70, 45)  #DoubleSidedSythe
    OceansSong = Weapons(79, 10, Elements.Water, "dualswords", "OceansSong", 130, 90)  #DualAquaticSwords
    TribalAxe = Weapons(50, 4, "forest", "axe", "TribalAxe" , -1, 10)
    GeneralsPower = Weapons(37, 19, Elements.Dark, "longsword", "GeneralsPower", -1 , -1)  #EvilLongSword
    FrozenFists = Weapons(-1, 13, Elements.Ice, "fists", "FrozenFists", -1, -1)  #FrozenFists
    Rake = Weapons(7, 4, Elements.Normal, "longsword", "Rake", 15 , 7)
    DevestationIncarnate = Weapons(30, 21, Elements.Toxic, "hammer", "DevastationIcarnate" , -1 , -1)
    Teeth = Weapons(-1, 2, Elements.Normal, "teeth", "Teeth", -1, 2)
    Phantaloom = Weapons(50, 7, Elements.Sky, "fan", "Phantaloom", 35, 25)
    SoldiersSword = Weapons(25, 5, Elements.Normal, "sword", "SoldiersSword", 25, 8)
    ElectricFins = Weapons(-1, 8, Elements.Electric, "fin", "ElectricFins", -1, 10)
    Toothblade = Weapons(50, 7, Elements.Normal, "sword", "Toothblade", 90, 60)
    SoldiersBow = Weapons(25, 5, Elements.Normal, "bow", "SoldiersBow", 50, 15)
    SoldiersHalberd = Weapons(25, 5, Elements.Normal, "spear", "SoldiersHalberd", 50, 15)
    DelayedPoison = Weapons(35, 13, Elements.Toxic, "dual swords", "DelayedPoison", 125, 90)
    Malestrom = Weapons(40, 15, Elements.Water, "sword", "Malestrom", 110, 80)