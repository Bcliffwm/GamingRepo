from src.Character import Character
from math import floor

class Enemy(Character):
    xpReward : int = 1
    
    def __init__(self, *args):
        super(Enemy, self).__init__(*args)
        self.set_xpReward()
        
    def set_xpReward(self):
        self.xpReward = floor(5* (self.xpReward) + (.25 * self.attack) + (.25 * self.defense))
    
    def award_xp(self):
        if(self.is_dead()):
            return self.xpReward
        else:
            return 0
    
    # Overloadded method - prints the xpReward in addition for enemy
    def print_info(self):
        print('Enemy information for: {}'.format(self.name))
        print('Is alive : {}'.format(not self.is_dead()))
        [print(val[0],":",val[1]) for val in vars(self).items() if val[0] != 'name']