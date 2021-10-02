import random
from elements import Elements
from textcolor import TextColor
class SideEffects:
  Burn      = 0 #Fire
  Poison    = 1 #Toxic
  Paralyzed = 2 #Electric
  Freezed   = 3 #Ice
  Blinded   = 4 #Dark
  Blessed   = 5 #Light
  
  side_effects_dict = {
    Elements.Fire : Burn,
    Elements.Toxic: Poison,
    Elements.Electric: Paralyzed,
    Elements.Ice  : Freezed,
    Elements.Dark : Blinded,
    Elements.Light: Blessed
  }

  #create a function to take in the element,  and a target
  def apply_side_effect (element, target, stance):
    percentage = random.randint(1,101)
    if percentage < 31:
      if stance == "defending":
        target.side_effect = SideEffects.side_effects_dict.get(element)
        #if then chain to examine what side effect the target now has...
        if target.side_effect == SideEffects.Burn:
          target.side_effect_dur = 3
          print(target.Name + " was " + TextColor.red +"burned!" + TextColor.white)
        elif target.side_effect == SideEffects.Poison:
          target.side_effect_dur = 5
          print(target.Name + " is now"+TextColor.brightgreen+ " poisoned!"+TextColor.white)
        elif target.side_effect == SideEffects.Paralyzed:
          target.side_effect_dur = 2
          print(target.Name+" has been "+TextColor.yellow+"Paralyzed!!!"+TextColor.white)
        elif target.side_effect == SideEffects.Freezed:
          target.side_effect_dur = 2
          print(target.Name + " was " + TextColor.blue + "frozen" + TextColor.white + " solid!")
        elif target.side_effect == SideEffects.Blinded:
          target.side_effect_dur = 5
          print(target.Name + " has been " + TextColor.black + "blinded!" + TextColor.white )
      else:
          target.side_effect_dur = 5
          target.Power += 6
          print(target.Name+" has been "+TextColor.magenta+"Blessed!!"+TextColor.white + " power is increased by 6!")
      # SideEffects.side_effects_dict.get(element) --> #will give the side effect per element