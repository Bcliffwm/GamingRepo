import Character
''' 
This class is the child class to Character that makes up players in game.
Keywords and attributes:
    level_up(self) - boolean function to check if the player levels up after a victory
    increase_level(self) - void function that increases level of the player
    increase_xp(self, xpReward) - void function that increases xp of the player after victory
    increase_stats(self) - void function that increases stats of player after a level up
'''
class Player(Character):
    def __init__(self, name: str):
        self.name = name
        
    def level_up_check(self) -> bool:
        if(self.xp > 100):
            return True

    def increase_xp(self, xpReward: int):
        self.xp += xpReward
    
    def increase_stats(self):
        self.attack += (self.attack * .3) + 1
        self.defense += (self.attack * .3) + 1
        self.hp += (self.attack * .6) + 3
        
    def increase_level(self):
        if(self.level_up_check()):
            self.xp -= 100
            self.level += 1
            self.increase_stats()




