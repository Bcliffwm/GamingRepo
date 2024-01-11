''' 
This class is the base class for all playable and non-playable characters in this RPG.

keywords:
    - name: Name of the character (str)
    - level: Level of the character (int)
    - experience: Experience of the character to decide a level up (int)
    - attack: Attack power of the character (int)
    - defense: Defense power of the character (int)
    - hp: Health Points of the character (int)

Key Methods:
    - attack_enemy(self, other) : Method to calculate damage output; used by both
    players and the enemies
    - receive_attack(self, other) : Method to calculate damage received;
    used by both players and enemies
    - reduce_health(self, damage) : Calculates the amount of health to reduce from
    amount of damage sustained
    - is_dead(self) : Boolean to determine if hp of character is reduced to 0
'''
from multiprocessing.sharedctypes import Value
from optparse import Values


class Character:
    #num_chars = 0 # tracker variable for number of characters initialized
    
    # Initialization function; Class Constructor
    def __init__(self, name: str, level: int = 1, exp: int = 0, atk: int = 1, defense: int = 1, hp:int = 1):
        # Class attributes
        self.name = name
        self.level = level
        self.experience = exp
        self.attack = atk
        self.defense = defense
        self.hp = hp
        
    # Show attributes
    def print_attributes(self):
        [print(val) for val in vars(self)]
     
    def print_info(self):
        print('Class information for: {}'.format(self.name))
        [print(val[0],":",val[1]) for val in vars(self).items() if val[0] != 'name']
        
    # Main function to check if character dies
    def is_dead(self):
        if(self.hp == 0):
            return True
        else:
            return False

    # Function for calculating damage output from playable character to enemy
    def attack_enemy(self, other) -> int:
        damage: int = self.attack - other.defense
        return damage
    
    # Function for calculating damage output from enemy to playable character
    def receive_attack(self, other) -> int:
        damage: int = other.attack - self.defense
        return damage
    
    # Function for calculating health point change after an attack
    def reduce_health(self, damage:int):
        self.health -= damage
    
    # Deconstructor function for class
    def __del__(self):
        print('Character: {} is deleted.'.format(self.name))
        #num_chars -= 1