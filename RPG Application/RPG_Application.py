from src import Player, Enemy

if __name__ == '__main__':
    p = Player.Player('My_Hero', 20, 100, 50, 50, 120)
    p4 = Enemy.Enemy('Enemy 4', 10, 10, 55, 30, 101)
   
    for i in range(0, 5):
        p.attack_other(p4)
    
    p4.print_info()
    p.is_kill(p4)
    p.print_info()