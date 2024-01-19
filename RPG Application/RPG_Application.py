from src import Player, Enemy, Battle

if __name__ == '__main__':
    p = Player.Player('My_Heroine', 20, 100, 50, 50, 120)
    p4 = Enemy.Enemy('Enemy 4', 10, 10, 55, 30, 55)
    
    p.save()
    