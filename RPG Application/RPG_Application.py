from src import Player, Enemy

if __name__ == '__main__':
    p = Player.Player('My_Hero', 99, 0, 999, 999, 99)
    #print(p.experience)
    
    p4 = Enemy.Enemy('Enemy 4', 40, 10, 55, 30, 80)
    

    p.attack_other(p4)
    #p4.reduce_health(p.attack)
    p4.is_dead()
    p4.print_info()
    p.print_info()