class Items:
  amount = 1
  name = ""
  price = 0
  sellPrice = 0
  story = False

  def __init__(self,noi,am=None,pr=None,spr=None):
    self.name = noi
    if am == None:
      self.story = True
    else:
      self.amount = am
      self.price = pr
      self.sellPrice = spr


# story_item = Item("cool stuff")
#regulor_item = Item("reg item",2,25,15)

  # def __init__(self, noi):
    
  #   self.name = noi

  # def getPrice():
  #   ##gh
  #   nothing here = nothing here
  story_dict = {
    "SuspicousScale" : "Reeve Pierce places the scale in the still waters of the luminescent pool and stands back as the monstrous form of the Wallubine forms above you."
  }
  