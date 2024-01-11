import os
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
class Character:
    # Initialization function; Class Constructor
    def __init__(self, name: str,
                 level: int = 1, 
                 exp: int = 0, 
                 atk: int = 1, 
                 defense: int = 1, 
                 hp:int = 1):
        # Class attributes
        self.files = []
        self.name = name
        self.level = level
        self.experience = exp
        self.attack = atk
        self.defense = defense
        self.hp = hp

    def __enter__(self):
        return self
    
    @property
    def name(self):
        return self.name
    @name.__setattr__
    def name(self, value):
        self.__name = value
    @property
    def level(self):
        return self.level
    @level.__setattr__
    def level(self, value):
        self.__level = value
    @property
    def experience(self):
        return self.experience
    @experience.__setattr__
    def experience(self, value):
        self.__experience = value
    @property
    def attack(self):
        return self.attack
    @attack.__setattr__
    def attack(self, value):
        self.__attack = value
    @property
    def defense(self):
        return self.defense
    @defense.__setattr__
    def defense(self, value):
        self.__defense = value
    @property
    def hp(self):
        return self.hp
    @hp.__setattr__
    def hp(self, value):
        self.__hp = value

    # Main function to check if character dies
    def is_dead(self):
        if(self.hp == 0):
            return True
        else:
            return False

    # Function for calculating damage output from playable character to enemy
    def attack_enemy(self, Base_Char: other) -> int:
        damage: int = self.attack - other.defense
        return damage
    
    # Function for calculating damage output from enemy to playable character
    def receive_attack(self, Base_Char: other) -> int:
        damage: int = other.attack - self.defense
        return damage
    
    # Function for calculating health point change after an attack
    def reduce_health(self, damage:int):
        self.health -= damage
    
    # Deconstructor function for class
    def __exit__(self, exc_type, exc_value, traceback):
        for file in self.files:
            os.unlink(file)