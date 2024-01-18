import Character, Player

class Enemy(Character):
    def __init__(self, name : str = "Enemy"):
        self.xpReward = xpReward
    
    def award_xp(self, other : Player):
        if(self.is_dead()):
            other.increase_xp(other, self.xpReward)