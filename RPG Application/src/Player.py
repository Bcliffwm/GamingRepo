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
        temp = self.attack
        self.attack += round((temp * .3)) + 1
        self.defense += round((temp * .3)) + 1
        self.hp += round((temp * .6)) + 3
        
    def increase_level(self):
        if(self.level_up_check()):
            self.xp -= 100
            self.level += 1
            self.increase_stats()
       
    def print_info(self, file):
        print('Name: {}'.format(self.name), file=file)
        print('Is alive: {}'.format(not self.is_dead()), file=file)
        [print(val[0],":",val[1], file=file) for val in vars(self).items() if val[0] != 'name']
        
    def save(self):
        with open('savefile.txt', 'r+') as f:
            self.print_info(f)

        

