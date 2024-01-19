from src.Character import Character
from src.Enemy import Enemy
''' 
this class is the child class to character that makes up players in game.
keywords and attributes:
    level_up(self) - boolean function to check if the player levels up after a victory
    increase_level(self) - void function that increases level of the player
    increase_xp(self, xpreward) - void function that increases xp of the player after victory
    increase_stats(self) - void function that increases stats of player after a level up
'''
class Player(Character):
    
    def __init__(self, *args):
        super().__init__(*args)
        
    def level_up_check(self) -> bool:
        if(self.xp >= 100):
            return True
        else:
            return False

    def is_kill(self, other:Enemy):
        if(other.is_dead() == True):
            self.increase_xp(other)
    
    def increase_xp(self, other:Enemy):
        self.xp += other.award_xp()
        self.increase_level()
        
    
    def increase_stats(self):
        self.attack += round((self.attack * .3)) + 1
        self.defense += round((self.attack * .3)) + 1
        self.hp += round((self.attack * .6)) + 3
        
    def increase_level(self):
        if(self.level_up_check()):
            self.xp -= 100
            self.level += 1
            self.increase_stats()

        

