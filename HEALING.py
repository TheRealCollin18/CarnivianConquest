from textcolor import TextColor
from items import Items
class Healing(Items):
  Heals = 0
  Magiks = 0
  ISITGIANT = False  #Tells whether or not it is a relatively large potion. Ex. basic potion = False and ultra potion = True 
  
  def __init__(self,NM,HE,AMO, IIG, MG, P, SP): 
    self.name = NM
    self.Heals = HE
    self.amount = AMO
    self.ISITGIANT = IIG
    self.Magiks = MG
    self.price = P
    self.sellPrice = SP

  def Add_Amount(self):#This will maybe still be here later on 
    self.amount += 1

  def use(self,target): 
    self.amount -= 1
    #this function controlls which of the two functions we will actually use
    if self.Heals == 0:
      self.MAGIK(target)
    else:
      self.HEAL(target)

  def MAGIK(self, target): #Magiks Reeve Pierce's Magik
    if self.Magiks + target.Magik > target.Max_Magik:
      target.Magik += target.Max_Magik - target.Magik
    else:
      target.hp += self.Magiks
    if self.ISITGIANT:
        print("Reeve Pierce chugs his " + self.name + " and " + TextColor.cyan + "replenishes" + TextColor.white , self.Magiks ,  "Magik")
    else:
        print("Reeve Pierce drinks his " + self.name + " and " + TextColor.cyan + " replenishes " + TextColor.white ,self.Magiks , " Magik")


  def HEAL(self, target): #Heals Reeve Pierce's hp 
    if self.Heals + target.hp > target.Max_hp:
      target.hp += target.Max_hp - target.hp 
    else:
      target.hp += self.Heals #Make sure the healing potion does not grant more health than you can have....
    if self.ISITGIANT:
        print("Reeve Pierce chugs his " + self.name + " and " + TextColor.green + "restores" + TextColor.white,self.Heals, "hp")
    else:
        print("Reeve Pierce drinks his " + self.name + " and " + TextColor.green + " heals" +TextColor.white ,self.Heals, " hp")
    