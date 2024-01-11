class Enemy(Character):
    def __init__(self, name : str = "Enemy",
                 xpReward: int = 5*(self.level) + (self.attack * .25) +
                 (self.defense * .25)):
        self.xpReward = xpReward
    
    def award_xp(self, Player: other):
        if(self.is_dead()):
            other.increase_xp(other, self.xpReward)