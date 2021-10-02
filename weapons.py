import random
class Weapons:
  #[durability, damage, element, typeofweapon]
  durability = 0
  maxDur     = 0
  damage     = 0
  maxDam     = 0
  broken     = False 
  element    = ""
  typeofweapon = ""
  name = ""
  price      = 0
  sellPrice = 0
    #this makes a specific weapon, with whatever is given
  def __init__(self,dur,d,e,typeof,nameof, p, sellp):
      self.durability = dur
      self.maxDur = dur
      self.damage = d
      self.maxDam = self.damage
      self.element = e
      self.typeofweapon = typeof
      self.name = nameof
      self.broken = False 
      self.price = p
      self.sellPrice = sellp

    #helper methods
  def use(self):
      if self.durability != -1:
        self.durability -= 1
        if self.durability < (self.maxDur/2) and not self.broken == 1:
            self.broken = 1
            self.damage /= 2
            print(self.name+" is broken! All damage will reduced by HALF!!")

  def reset(self):
    self.durability = self.maxDur
    self.damage = self.maxDam
    self.broken = 0
    
  def repair(self):
      self.durability = self.maxDur
      self.damage = self.maxDam
      self.broken = 0
      print(self.name+" has been repaired, all stats restored!")
  #gives the sentence to better show off the difference of each weapon 
  #For example: for sword it prints "Reeve Pierce slashes" while for spear it prints "Reeve Pierce repeatedly attacks"
  def getSaying(self,name,EnemyName,Damage):
      return {
          "spear": name +" charges up his " + self.name + " and repeatedly attaks the " + EnemyName + " dealing "+Damage+"damage!",    
          "sword": name + " draws his " + self.name + " and slashes at the "+ EnemyName + " dealing " + Damage + " damage!",
          "longsword": name + "draws his " + self.name + " and strongly swings it towards " + EnemyName + " dealing " + Damage + " damage!",
          "fists": name + " prepares himself and sends out a flurry of punches using his " + self.name + " finishing the " + EnemyName + " with a sky uppercut dealing " + Damage +" damage",
          "bow": name + " takes aim at " + EnemyName + " with his " + self.name + "and shoots an arrow that plunges into the " + EnemyName + "'s torso dealing " + Damage + " damage!",
          "dualswords" : name + " draws both of his " + self.name + "s and cross chops the " + EnemyName + " dealing " + Damage + "damage!",
          "axe" : name +" jumps up into the air, lifting his " + self.name + " and slices " + EnemyName + " dealing " + Damage + "damage!",
          "fan" : name + " swings his " + self.name + " blowing a strong gust of wind dealing" + Damage + " damage to " + EnemyName + "!",
          "rake" : name + " rakes " + EnemyName + " using his " + self.name + " dealing " + Damage + "damage!",
          "hammer" : name + " slams his " + self.name + " into the ground sending out a shockwave that deals " + Damage + " damage to " + EnemyName + "!",
          "sythe" : name + " swings his " + self.name }.get(self.typeofweapon)

 

            

#say we are in main
# sword = Weapons(5,10,"none","sword")

