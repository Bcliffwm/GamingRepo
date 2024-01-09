class Base_Char:
    def __init__(self, name, level, exp, atk, defense, hp):
        self.name = name
        self.level = level
        self.experience = exp
        self.attack = atk
        self.defense = defense
        self.hp = hp
    
    
    # Main function to check if character dies
    def is_dead():
        if(hp == 0):
            return True
        else:
            return False
