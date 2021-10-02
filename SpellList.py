from AttackMagik import AttackMagik
from SupportMagik import SupportMagik
from elements import Elements

#AttackSpells: :) :/
#Damage, Element, NameoSpell, MagikSaying, SideEffect, Magik
class SpellList:
    GalacticSpear = AttackMagik(15, Elements.Cosmic, "GalacticSpear", "Ennoz Pursea!", "Wearzzz", 5)

    MeteorSlam = AttackMagik(14, Elements.Cosmic, "StarShine", "Estrillo Debect", "sraeW", 6)
    
    DrakeBlast = AttackMagik(15, Elements.Fire, "DrakeBlast", "Snogard Gardolar!!", "Wear", 5)

    Erupt = AttackMagik(16, Elements.Fire, "Erupt", "Moledok Jabict", "Wearxxx", 5)

    Quake = AttackMagik(15, Elements.Earth, "Quake", "Robesq Ebeben!", "Wear", 5)

    RelentlessAvalanche = AttackMagik(18, Elements.Earth, "RelentlessAvalanche", "Leantie Nagstao!", "Wearzsz", 9)

    NaturesFury = AttackMagik(16, Elements.Forest, "NaturesFury", "Derv fa Eruten!", "Wearz",3)

    BrambleBash = AttackMagik(15, Elements.Forest, "BrambleBash", "Ostruzun Kakamai!", "WEARSS", 6)

    ScaldingWave = AttackMagik(15, Elements.Water, "ScaldingWave", "Gavan Kivese!", "Wears", 5)

    HyperCurrent = AttackMagik(13, Elements.Water, "HyperCurrent", "Rephie Stromorg!", "WEerz", 4)

    WindsOfMight = AttackMagik(14, Elements.Sky, "WindsofMight", "Dednoot ilalai!", "Wearx", 6)

    ElectroSlam = AttackMagik(16, Elements.Electric, "ElectroSlam", "Trikeliemo Salime!", "WWeers", 6)

    DarkestNight = AttackMagik(16, Elements.Dark, "DarkestNight", "Bukus Obemnya!", "Wears", 6)

    BlindingLight = AttackMagik(16, Elements.Light, "BlindingLight", "Locoo Mondrome!", "Wears", 6)

    PoisonSpray = AttackMagik(14, Elements.Toxic, "PoisonSpray", "Rapras Henimie!", "Wears", 6)

    Virus = AttackMagik(14, Elements.Tech, "Virus", "Rasai Inubang", "WWeaarS", 6)

    SonicBoom = AttackMagik(15, Elements.Sound, "SonicBoom", "Slunekcý Krest", "WEARS", 6)

    Blizzard = AttackMagik(16, Elements.Ice, "Blizzard", "Tempasta Yuweigan", "Waearsrdde", 7)
    
    PhasmaOrb = AttackMagik(8, Elements.Dark, "PhasmaOrb", "Atamorsk Atibro", "Wears", 3)



    attack_spells = [NaturesFury, GalacticSpear, SonicBoom]#GalacticSpear,DrakeBlast,Erupt,Quake,RelentlessAvalanche,#BrambleBash,ScaldingWave,HyperCurrent,WindsOfMight,ElectroSlam,DarkestNight,BlindingLight,PoisonSpray,Virus]
    #Remember when adding a spell to add the SupportMagik. ect to it
    support_spells = ["ReturnToSender", "Empower", "HeavensBlessing", "FullShield"]