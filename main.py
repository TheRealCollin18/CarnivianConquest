#hello! Hola
#Medeival Adventure Setting
from Controller import Controller
from textcolor import TextColor
from armory import armory 

#print something, check if the response if yes or n, repeat if not...

def yesNoGetter(text):
    exit = False
    val = False
    while not exit:
        res = input(text)
        if res.upper()[0] == "Y":
            val = True
            exit = True
        elif res.upper()[0] == "N":
            val = False
            exit = True
        else:
            print("Enter 'Y' or 'N'!")
            exit = False
    return val

#which ever is the last color you use, is the one that will be used for later prints.

# def Demo():
#   while True:
#     controller = Controller()
#     input(" Press *Enter*"  " to continue with the storyline")
#     print("__Carnivian Conquest__")
#     input("Creators: Collin James Lara and William. Enjoy the Demo :)!")
#     input("\n-----------------------------------\nThe morning fog brought a silent dread to the Carnivian Army as they stood tall, protecting the capital city of Carnivia, Ransham. The general Orion stood unfazed commanding the front lines as the Devil King's army approached from the west. Civilized yet Crude the enemy army stalked closer until the Devil King's army sounded their horns and rushed forward with a lust for blood.  When the clashing of swords and battle cries rang through Reeve Pierce's ears, He knew that there was no escape from the horrors ahead.")
#     input("He didn't know why he was here.")
#     input("He didn't know why he had a shield and sword in my hand")
#     input("All he knew was that he needed to RUN. Reeve Pierce bolted back to the castle walls, where amist all the chaos an Earthborn confronted him. It's deformed structure paralysed him with fear and chilled him to the very core. Frozen in place, the Earthborn attacked")
#     if not controller.battle1():
#         if yesNoGetter("\nYou have died, restart? "):
#             return True
#         else:
#             return False
#     #check to see if Reeve Pierce is dead....
#     # input("Reeve was battered, but victorious. The Earthborn had been defeated at his own hands, yet there was still so much that was left unknown. As If like a dream, ")
#     input("'You're a mage?' Orion questioned looking at Reeve Pierces glowing hands.\n 'I don't know' Reeve Pierce said \n Suddenly the screeching of something in the distance exploded the bridge from under their feet, causing them to plummet into the river below.")
#     input("Reeve Pierce awoke alone lying on the swampy floor. As he regained his footing, he noticed the red glare of a blood streaked sky overhead the capital city. Reeve Pierce slowly and carefully examined the nearby area finding Orion lying on the floor almost looking half alive.")
#     input(" Orion awoke slowly as Reeve Pierce ran over to him. He was badly wounded and his longsword layed beside him mostly broken. Suddenly Orion's eyes lit up as he weakly pointed at an approaching wolfbear. Reeve Pierce quickly grabbed Orion's longsword and prepared himself for the conflict...")
#     #fight sequence here
#     if not controller.battle2():
#         if yesNoGetter("\nYou have died, restart? "):
#             return True
#         else:
#             return False
#     input("'Kid come here' General Orion coughed out. Reeve Pierce turned around to face him as he regained his stregth.'I've seen you fight. You fight with courage and confidence in the face of extreme danger. You even wielded my longsword, Sinstained!' He reached into his pocket and pulled out a map. 'This is a map to the town of RaddishVille where you will find the mage, Iskall. He is the only one who can maybe stop this catastrophe.' Reeve Pierce nodded and with a surge of confidence, ventured into the unknown to save Carniva. The beggining of the story of the great Carnivian Conquest!")
#     print("Thank you for playing our demo. Hope you enjoyed!")
def Wallubine_Swamp():
  input("Chapter one")
  input("The Wallubine")
  input("Reeve got tired quickly traversing the swampy terrain in almost broken shoes. He had been traveling for many days seeing smoke still staining the sky. As night approached Reeve saw a town on stilts in the distance. Reeve Pierce studied the sign reading, 'Terford town    The diamond of gravel lake'. Allthough there was an etched out warning reading,'Beware of the Wallubine The terror of Gravel lake'. He was curious of this and approached two fisherman engaing in a conversation on the Wallubine. One was shorter with a think beird and straping overalls while the other was tall and lanky with a rather large backpack strapped around his back. The shorter fisherman noticed that Reeve Pierce had barged in on the conversation and said 'Well howdy young traveler if you are thinking of crossing that there lake, that devil fish will swallow your boat whole. Could be a good idea to stick to the shore if you still want all your bones intact.' The taller fisherman added, 'And thank the Angle Almighty that we were able to swim ashore while that their beast ate our supply of Gourmet fish bait.'")
  input("Reeve Pierce asked how he could travel to town with the Wallubine in the water. The shorter fisherman said 'Since the battle at Ransham, people like us haven't been able to figured out how to travel back and forth to the town without any threat from the Wallubine'. Reeve Pierce was dissapointed by this. The shorter fisherman noticed this and said.'However We have heard that to the east lies the Wallubines den. Maybe you could tame it'. The taller one further mocked, 'Yeah and maybe make fishes fly!'. They almost fell done laughing at this and Reeve Pierce thanked them for the info. He made a promise to help whenever they needed assistance and strode off. Reeve Peirce, although a little frazzled,  continued on towards Gravel lake. He then stopped on the eastern shores to investigate the Wallubine further")
# controller.WallubineSwamp()
# controller.inBetweenEncouter() -> Merchant, Explorable areas ->

  #create a fuction where he can chose either to buy things from the mechant, go into cave to kill things for money and resources, or look at the view. - 
def Merchant_Cryle():
  buystuff = input(" have many things to sell, would you like to know how to buy from me? (Y/N)")
  if buystuff == "Y":
    input("Hello my name is Cryle, a world class merchant selling only the most extroadinary artifacts and weapons from Terford town to Fafnir bay.")
    input("Although before we start, I need you to slay the Wallubine. That malicious beast is cutting off my trading routes to Terford town. Really bad for buisness. To aid you in your quest I give you my finest sword from the eastern forests. ")
    input("Hopefully this is the start of a wonderful buisness relationship! And as always, thank you come again!")
  else:
    input("but if you ever change your mind, make sure to stop by my shop, open at every major store from dawn to dusk.") 
    input("Thank you come again!")
def Cave_Encounters(): 
  FloorLevel = 0
  while(True):
    f = "f" 

def Demastia():
  input("Chapter two")
  input("Blackened Skies")
  input("Of all the cities in Western Carnivia, Demastia was known to be the most defended and advanced in all forms of military and technology. So much so that it was nicknamed 'The City of Dreams'. Reeve Pierce and the rest of the rookie soldiers were told these rumors. Going to Demastia was one of the few things that Reeve pierce dreamed to do.") 
  input("Despite having the urge to visit the city he was still uterly lost in the middle the swamp. Then suddenly an explosion shook the heavens. As Reeve Pierce headed towards the smoke, a civilian running in the oposite direction gasped out, 'The Devil King's army, they're tearing through the city! I see Orion's sword on your back, so please you must help us!' Suddenly surging with confidence, Reeve Pierce drew his sword and charged into the flames of the former city of dreams, Demastia.")
  #insert fighting sequence agaisnt the devil king's army with him eventualy reaching the general of the army. Ill continue the story of this section once we do that.
  input("Reeve Pierce exited the capital, mortally wounded from the generals brutal and unorthadox fighting style. He clutched his stomach and sat on the cold stone stairway. Beside him lay a half burnt doll, most likely from one of the citizens of Demastia. It was worn out, but still showed the childlike design on its face.")
  input("Reeve Pierce, at that moment, felt a burning sensation deep in his chest. He felt deep sadness.")
  input("Sadness for not being able to do something to save these people with his one chance to do something. This sadness suddenly fueled a powerful anger for The Devil King and his army pushing him to leave the cold steps and rise into the sunlight with a new objective. Destroy the Devil King.")

    
def TheMagikWoods():
  input("Chapter three")  
  input("Voices Inside")
  input("Leaving the burning city of Demastia, Reeve Pierce needed a place to rest and recover. So he took a right to the nearby town, Runetown. As he entered the woods that the town resided, his mind began to vibrate with ideas and thoughts that he couldn't comprehend, but for some reason they called to him from the woods. Reeve Pierce slowly tip toed through the boreal trees, with even more voices screaming inside him. ")
  input("Reeve Pierce grasped his head in agony and kneeled on the ground. The voices became lounder and lounder and then-")
  input("LOOK OUT!")
    #create inventory for Character
  input("Reeve Pierce beaten up continued back into the woods. Now it seemed like he was being controlled like a puppet. He was so tired and wanted to collasp onto the ground, but something kept me going. After what seemed like hours, I stopped and fell onto the soft grass. This seeming pillow from heaven drifted him into a deep sleep.")
  input("")
  input("")
def Lorulia_town():
  input("Chapter five")
  input("The Runaway Princess")
  input("Reeve Pierce wore a carefree grin striding to his next destination. His past victories against the evil forces plauging the land of Carnivia skyrocketed his confidence to new heights. But still he still had a lump on the back of his throat keeping him from fully swallowing this.")
  input("These battles seem strangely easy. The size of the Wallubine seemed noticabl smaller than people described. The amount of Ogres guarding the general of destruction. Was it all a ploy! Was it all a-")
  input("'Excuse me sir!'")
  input("A woman in a flowing blue dress ran towards him, her heels clattering on the stone brick path. Before he could stop her, she bolted past him off of the path and into the borderline woods. ")
  input("'Hey you!', a soldier in a red jacket asked panting, 'You are a Ransham royal guard, chase after the princess of Lorulia!'")
  input("Startled, Reeve Pierce runs to into the woods to search for the princess. ")#insert another sequence like the Wallubine swamp one


    
# playing = Demo()
# while playing:
#     playing = Demo()


#testing
def GameSquence(self):
  controller = Controller()
  while controller.ReevePierce.money > 0:

    self.Wallubine_Swamp()
    
    if controller.EAS() == False:
      print("You ascend to the heavens, dead. The gods then deem you worthy of starting again.")
      if yesNoGetter("Would you like to play again"):
        controller.ReevePierce.money -= controller.ReevePierce.money/2 
        continue 
      else: 
        print("Reeve Pierce dies with the dream of saving Carnivia and its people. Your journey ends here.")
        print("Thanks for playing!")
        print("Carnivia Conquest by:Collin and William ")
        return False 
    else:
      break 

    





# ReevePierce = Character()
# #give this the durability, damage, element, type of weapon, name of weapon
# NewWeapon = Weapons(45, 7, "Cosmic", "Spear", "Rhanash")
# ReevePierce.equipWeapon(NewWeapon)
# ReevePierce.addAttackSpell(CrypticSpear)
# ReevePierce.addAttackSpell(DragonsWrath)
# ReevePierce.addAttackSpell(Quake)
# ReevePierce.addAttackSpell(NaturesFury)
# ReevePierce.addAttackSpell(BrambleBash)
# ReevePierce.addAttackSpell(ScaldingWave)
# ReevePierce.addAttackSpell(DarkestNight)
# ReevePierce.addAttackSpell(BlindingLight)
#  #Weapons(34, 18, "Forest", "Axe", "WoodlandAxe")
# WoodenSpear = Weapons(12, 2, "none", "Spear", "WoodenSpear")



# #hp, weapon, name, armor, element, level
# #Enemies:
# MountainGnome = Enemies(14, WoodenSpear, "MountainGnome", 3, Elements.Forest, 3, 14, 4, False, True)

# #while(1):
# #   if ReevePierce.isDead() == False:
# #     ReevePierce.CastAttackSpell(0, MountainGnome)
# #   if ReevePierce.isDead() == True:
# #     break
# #   if MountainGnome.isDead()== False:
# #     MountainGnome.AttackEnemy(ReevePierce)
# #   if MountainGnome.isDead() == True:
# #     break


# fightSequence(ReevePierce, MountainGnome)

  