import random
from elements import Elements
from SpellList import SpellList
from textcolor import TextColor
from sideeffects import SideEffects
class Enemies:
  hp = 0
  maxhp = 0
  magik = 0
  max_magik = 0
  weapon = ""
  Name = ""
  armor = 0
  element = ""
  level = 0
  Power = 0
  spell_move = {}
  ambiance = ""
  expyield = 0
  element = ""
  twoelement = ""
  hm = False
  hw = False
  side_effect = None
  side_effect_dur = 0
  
#   def __init__(self, hp, w, n, a, e, l, ab, maxhp, ex, hm):
  def __init__(self, hp, w, n, a, e, l, maxhp, ex, hm, mk,maxmk, am, te, po):
    
    self.weapon = w
    self.Name = n
    
    self.element = e
    self.level = l
    # self.ability = ab
    self.maxhp = maxhp
    self.expyield = ex
    self.hm = hm
    self.magik = mk
    self.max_magik = maxmk
    self.hw = not self.weapon == ""
    self.ambiance = am
    self.twoelement = te

    self.Power = po
    self.hp = hp
    self.armor = a

    #need to make this into its own method for the enemy to use...
    for i in range(self.level):
     help = random.randint(1,3)
     self.Power += random.randint(1,2)
     self.hp += help 
     self.maxhp += help
    
     


    self.spell_move = {
      Elements.Cosmic : SpellList.GalacticSpear,
      Elements.Fire : SpellList.Erupt,
      Elements.Water : SpellList.HyperCurrent,
      Elements.Earth : SpellList.Quake,
      Elements.Sky : SpellList.WindsOfMight,
      Elements.Electric : SpellList.ElectroSlam,
      Elements.Light : SpellList.BlindingLight,
      Elements.Dark : SpellList.PhasmaOrb,
      Elements.Forest : SpellList.NaturesFury,
      Elements.Toxic : SpellList.PoisonSpray,
      Elements.Tech : SpellList.Virus, 
      Elements.Ice : SpellList.Blizzard,
      
    }

  #enemy.reset()

  def set_level(self,new_level):
    self.level = new_level

  def reset(self, user):
    user.hp = user.maxhp
    user.magik = user.max_magik
    user.side_effect = None
    user.side_effect_dur = 0
    user.weapon.reset()

  def EnemyMove(self, user):
    # RandomMove = random.randint(1,2)
    RandomMove = 2
    while True:
      print(RandomMove)
      if RandomMove == 1 and self.hw == True:
          elementBonus = Elements.TypeMachups(self.weapon.element, user.element)
          DamageInAll = (self.weapon.damage + self.Power/2) * elementBonus + random.randint(-1,1)
          self.weapon.use()
          print(self.Name + " uses his " + self.weapon.name + " to attack " + user.Name)
          print("POW! " + self.Name + " dealed", DamageInAll, "to", user.Name)
          if elementBonus < 1:
            print(TextColor.orange+"It was Not Very Effective...", TextColor.white)
          elif elementBonus > 1:
            if elementBonus == 2:
              print(TextColor.brightgreen+"It was Super Effective", TextColor.white)
            elif elementBonus == 4:
              print(TextColor.brightgreen+"It was EXTREMELY EFFECTIVE!!")
          elif elementBonus == 0:
            print("It had no effect!")
          user.takeDamage(DamageInAll)
          break
      elif RandomMove == 2 and self.hm == True and self.spell_move.get(self.element).Magik <= self.magik: 

        spell = self.spell_move.get(self.element)
        print(self.Name + " chants " + spell.MagikSaying + "!!!")
        elementBonus = Elements.TypeMachups(spell.Element, user.element)
        DamageInAll = spell.Damage * elementBonus
        print("BANG! " + self.Name + " casts " + spell.NameoSpell + " and dealed ", DamageInAll, " to Reeve Pierce!" )
        if elementBonus < 1:
          print(TextColor.orange+"It was Not Very Effective...", TextColor.white)
        elif elementBonus > 1:
          if elementBonus == 2:
            print(TextColor.brightgreen+"It was Super Effective", TextColor.white)
          elif elementBonus == 4:
            print(TextColor.brightgreen+"It was EXTREMELY EFFECTIVE!!")

        SideEffects.apply_side_effect(spell.Element, self,"attacking")

        SideEffects.apply_side_effect(spell.Element, user,"defending")
        
        self.magik -= spell.Magik

        user.takeDamage(DamageInAll)
        break
      else:
        RandomMove = 1

     

  def TDE(self, damageInflicted):
    healthBefore = self.hp
    self.hp -= damageInflicted - self.armor
    if self.isDead():
        print(self.Name+" has perished...")
    if self.hp > healthBefore:
        self.hp = healthBefore
        print(self.Name+"'s armor repelled the damage")

    if not self.isDead():
        print(self.hp, " / "+ str(self.maxhp)+ " HP left on the " + self.Name)
    if self.hp > self.maxhp:
      self.hp = self.maxhp

  def isDead(self):
      return self.hp <= 0 

  def printHp(self):
        print(self.hp, "/", self.maxhp)

  # def Abilities():
  #   j
  #spell_move = {
  #  Elements.Forest : SpellList.NaturesFury,
  #  Elements.Cosmic : 
  #}