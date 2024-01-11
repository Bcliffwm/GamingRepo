from src import Player, Enemy

if __name__ == '__main__':
    
    p2 = Player.Player('Ray', 10, 2, 3, 5, 55)
    #p2.print_attributes()
    p2.print_info()
    print(p2.level_up_check())
