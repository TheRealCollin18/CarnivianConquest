from enum import Enum
class Elements(Enum):
    Cosmic = 0
    Fire = 1
    Water = 2
    Earth = 3
    Sky = 4
    Electric = 5
    Light = 6
    Dark = 7
    Forest = 8
    Toxic = 9
    Tech = 10
    Sound = 11
    Ice = 12
    Normal = 13
    def ElementOAttackSpell(User,Enemy):
      print( User.AttackSpell.Element)

    def toString(self):
      if self == Elements.Cosmic:
        return "Cosmic"
      elif self == Elements.Fire:
        return "Fire"
      elif self == Elements.Water:
        return "Water"
      elif self == Elements.Earth:
        return "Earth"
      elif self == Elements.Sky:
        return "Sky"
      elif self == Elements.Electric:
        return "Electric"
      elif self == Elements.Light:
        return "Light"
      elif self == Elements.Dark:
        return "Dark"
      elif self == Elements.Forest:
        return "Forest"
      elif self == Elements.Toxic:
        return "Toxic"
      elif self == Elements.Tech:
        return "Tech"
      elif self == Elements.Sound:
        return "Sound"
      elif self == Elements.Ice:
        return "Ice"
      else:
        return "Normal"
        


    def TypeMachups(Element1,Element2):
    #   Water Fire Ground Grass
    # W   N    S     S      N
    # F   N    N     E      S
    # G   S    N     S      N
    # Gr  E    S     E      E
    # Each of the Elements has a number equivalent, that we can bind to a index of a list
    # Elements.Cosimic --> 0
    #[ [] ]
    #{ {} }
      return {
        Elements.Cosmic: { #COSMIC START
          Elements.Cosmic: 0.6,
          Elements.Fire: 2,
          Elements.Water: 2,
          Elements.Earth: 0.6, 
          Elements.Sky: 0.6,
          Elements.Electric: 1,
          Elements.Light: 0,
          Elements.Dark: 0,
          Elements.Forest: 2,
          Elements.Toxic: 2, 
          Elements.Tech: 1,
          Elements.Sound: 2, 
          Elements.Ice: 1, 
          Elements.Normal: 1,
          },
        Elements.Fire: { #FIRE START
          Elements.Cosmic: 0.6,
          Elements.Fire: 0.6,
          Elements.Water: 0.6,
          Elements.Earth: 1, 
          Elements.Sky: 1,
          Elements.Electric: 1,
          Elements.Light: 1,
          Elements.Dark: 1,
          Elements.Forest: 2,
          Elements.Toxic: 2,
          Elements.Tech: 2,
          Elements.Sound: 1,
          Elements.Ice: 2,
          Elements.Normal: 1,
        },
        Elements.Water: { #WATER START
          Elements.Cosmic: 0.6,
          Elements.Fire: 2,
          Elements.Water: 0.6,
          Elements.Earth: 2,
          Elements.Sky: 1,
          Elements.Electric: 1,
          Elements.Light: 1,
          Elements.Dark: 1,
          Elements.Forest: 0.6,
          Elements.Toxic: 0.6,
          Elements.Tech: 2,
          Elements.Sound: 2,
          Elements.Ice: 0.6,
          Elements.Normal: 1,
        },
        Elements.Earth: { #EARTH START
          Elements.Cosmic: 0.6,
          Elements.Fire: 2,
          Elements.Water: 1,
          Elements.Earth: 1, 
          Elements.Sky: 0,
          Elements.Electric: 4,
          Elements.Light: 1,
          Elements.Dark: 1,
          Elements.Forest: 1,
          Elements.Toxic: 2,
          Elements.Tech: 1,
          Elements.Sound: 1,
          Elements.Ice: 0.6,
          Elements.Normal: 1,
        },
        Elements.Sky: { #SKY START
          Elements.Cosmic: 1,
          Elements.Fire: 2,
          Elements.Water: 1,
          Elements.Earth: 1, 
          Elements.Sky: 1,
          Elements.Electric: 0.6,
          Elements.Light: 2,
          Elements.Dark: 2,
          Elements.Forest: 2,
          Elements.Toxic: 1,
          Elements.Tech: 0.6,
          Elements.Sound: 1,
          Elements.Ice: 0.6,
          Elements.Normal: 1,
        },
        Elements.Electric: { #ELECTRIC START
          Elements.Cosmic: 2,
          Elements.Fire: 1,
          Elements.Water: 2,
          Elements.Earth: 0, 
          Elements.Sky: 2,
          Elements.Electric: 0.6,
          Elements.Light: 0.6,
          Elements.Dark: 2,
          Elements.Forest: 0.6,
          Elements.Toxic: 0.6,
          Elements.Tech: 2,
          Elements.Sound: 2,
          Elements.Ice: 0.6,
          Elements.Normal: 1,
        },
        Elements.Light: { #LIGHT START
          Elements.Cosmic: 2,
          Elements.Fire: 1,
          Elements.Water: 0.6,
          Elements.Earth: 1, 
          Elements.Sky: 0.6,
          Elements.Electric: 1,
          Elements.Light: 1,
          Elements.Dark: 4,
          Elements.Forest: 0,
          Elements.Toxic: 1,
          Elements.Tech: 1,
          Elements.Sound: 1,
          Elements.Ice: 1,
          Elements.Normal: 1,
        },
        Elements.Dark: { #DARK START
          Elements.Cosmic: 0.6,
          Elements.Fire: 1,
          Elements.Water: 1,
          Elements.Earth: 1, 
          Elements.Sky: 0.6,
          Elements.Electric: 1,
          Elements.Light: 4,
          Elements.Dark: 1,
          Elements.Forest: 2,
          Elements.Toxic: 0.6,
          Elements.Tech: 1,
          Elements.Sound: 1,
          Elements.Ice: 1,
          Elements.Normal: 1,
        },
        Elements.Forest: { # FOREST START
          Elements.Cosmic: 0.6,
          Elements.Fire: 0.6,
          Elements.Water: 2,
          Elements.Earth: 2, 
          Elements.Sky: 0.6,
          Elements.Electric: 0.6,
          Elements.Light: 2,
          Elements.Dark: 0.6,
          Elements.Forest: 0.6,
          Elements.Toxic: 0.6,
          Elements.Tech: 1,
          Elements.Sound: 1,
          Elements.Ice: 1,
          Elements.Normal: 1,
        },
        Elements.Toxic: { #TOXIC START
          Elements.Cosmic: 0.6,
          Elements.Fire: 0.6,
          Elements.Water: 0.6,
          Elements.Earth: 0, 
          Elements.Sky: 1,
          Elements.Electric: 1,
          Elements.Light: 4,
          Elements.Dark: 1,
          Elements.Forest:2,
          Elements.Toxic: 0.6,
          Elements.Tech: 0.6,
          Elements.Sound: 1,
          Elements.Ice: 0.6,
          Elements.Normal: 1,
        },
        Elements.Tech: { #TECH START
          Elements.Cosmic: 1,
          Elements.Fire: 1,
          Elements.Water: 0.6,
          Elements.Earth: 2, 
          Elements.Sky: 1,
          Elements.Electric: 0.6,
          Elements.Light: 1,
          Elements.Dark: 1,
          Elements.Forest: 1,
          Elements.Toxic: 2,
          Elements.Tech: 2,
          Elements.Sound: 0.6,
          Elements.Ice: 2,
          Elements.Normal: 2,
        },
        Elements.Sound: { #SOUND START
          Elements.Cosmic: 0.6,
          Elements.Fire: 1,
          Elements.Water: 0.6,
          Elements.Earth: 0.6, 
          Elements.Sky: 1,
          Elements.Electric: 1,
          Elements.Light: 2,
          Elements.Dark: 0.6,
          Elements.Forest: 1,
          Elements.Toxic: 0.6,
          Elements.Tech: 2,
          Elements.Sound: 0,
          Elements.Ice: 1,
          Elements.Normal: 4,
        },
        Elements.Ice: { #ICE START
          Elements.Cosmic: 1,
          Elements.Fire: 1,
          Elements.Water: 2,
          Elements.Earth: 2, 
          Elements.Sky: 2,
          Elements.Electric: 0.6,
          Elements.Light: 1,
          Elements.Dark: 1,
          Elements.Forest: 2,
          Elements.Toxic: 2,
          Elements.Tech: 0.6,
          Elements.Sound: 0,
          Elements.Ice: 0.6,
          Elements.Normal: 1,
        },
        Elements.Normal: { #NORMAL START
          Elements.Cosmic: 0.6,
          Elements.Fire: 1,
          Elements.Water: 1,
          Elements.Earth: 1, 
          Elements.Sky: 1,
          Elements.Electric: 1,
          Elements.Light: 1,
          Elements.Dark: 1,
          Elements.Forest: 1,
          Elements.Toxic: 1,
          Elements.Tech: 0.6,
          Elements.Sound: 1,
          Elements.Ice: 1,
          Elements.Normal: 1,
        }
      }.get(Element1).get(Element2)
    #196!!!!!?!?!?!??!?!?!?!?!??!q1!??
    
