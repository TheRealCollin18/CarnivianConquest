import Magik
# from enemies import Enemies 


# sup = SupportMagik()
# sup.ReturnToSender(ReevePierce, enemy)
# rts(self, user, enemy)
# ReevePierce.sup_mag_dict.get("ReturnToSender")

MagikCost = 0

class SupportMagik:
    TypeoSpell = ""
    Element = ""
    debuff_spell = None
        
    # def __init__(self, TOS, E, NOS, MS, SE, TL):
    #   self.TypeoSpell = TOS
    #   self.NameoSpell = NOS
    #   self.MagikSaying = MS
    #   self.SideEffect = SE
    #   self.Timeleft = TL

    #SupportSpells
    def ReturnToSender(self, user, enemy):
        self.Magik = int((user.Magik * (1/2)) + 1)
        print(user.Name + " siletly chants Zami Hyke.. and readies himself")
        user.Magik -= self.Magik
        user.held_move = self.ReturnToSender2
        user.waitTurn = True

    def ReturnToSenderCost(user):
        return (user.Magik * (1/2)) + 1

    def ReturnToSender2(self, user, enemy):
        RTS_Damage =  user.DFE * 2
        if RTS_Damage == 0:
          
          print("Nothing happened!")#say it failed....
        print(user.Name + " lifts up his hand with magenta glowing eyes and yells JAMACIA!! This deals", RTS_Damage , "!")
        user.held_move = None
        enemy.TDE(RTS_Damage)

    def Empower(self, user, enemy):
        self.Magik = 11
        user.time_left = 2
        user.Power += 5
        print(user.Name + "chants Tuxhawby Naq! and raises Reeve Pierce's power by 5 stages for 1 turn")
        SupportMagik.debuff_spell = SupportMagik.debuffEmpower
        
    def EmpowerCost(user):
        return 11

    def debuffEmpower(user):
        user.Power -= 5
        print("Reeve Pierces buffs petered out!")
        SupportMagik.debuff_spell = None

    def HeavensBlessing(self, user, enemy):
        self.Magik = 11
        user.time_left = 4
        user.Armor += 10
        print(user.Name + " absorbs the sun's energy and chants, Ebno Aled Cielo! This raises " + user.Name + "'s armor by 10 for 3 turns")
        SupportMagik.debuff_spell = SupportMagik.debuffHeavensBlessing

    def HeavensBlessingCost(user):
        return 11

    def debuffHeavensBlessing(user):
        user.Armor -= 10
        print("Reeve Pierces buffs petered out!")
        SupportMagik.debuff_spell = None

        
    def DeimensionalWarp(self, user, enemy):
        self.Magik = 8
        #finish when did elements

    def FullShield(self, user, enemy):
      self.Magik = (user.Magik * 2/3)
      user.time_left = 2
      user.Armor += 999999
      print(user.Name + "chants ,Gavardin Exetrop! This creates a huge shield that fully protects " + user.Name + (" from any outside damage for 1 turn"))
      SupportMagik.debuff_spell = SupportMagik.debuffFullShield

    def FullShieldCost(user):
        return user.Magik * 2/3
    
    def debuffFullShield(user):
      user.Armor -= 999999
      print("Reeve Pierces buffs petered out!")
      SupportMagik.debuff_spell = None
      
    def ElectroMagnetism(user):
      #finish when elements are done 
      SOMETHING = "gh"
    #this dictionary allows us to run a function with just the name of the spell
    sup_magik_dict = {
        "1" : ReturnToSender, 
        "2" : Empower,
        "3" : HeavensBlessing,
        "4" : FullShield,
    }

    #this dictionary allows us to see the magik cost for any spell by name
    sup_magik_cost_dict = {
      1 : ReturnToSenderCost,
      2 : EmpowerCost,
      3 : HeavensBlessingCost,
      4 : FullShieldCost,
    }

