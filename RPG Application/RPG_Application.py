from src import Player, Enemy, Battle, Menu

if __name__ == '__main__':
    running = True
    Menu.display_starting_screen()
    selection = ''
    
    while running:
        
        selection = Menu.display_menu()
        if selection.lower() == 'q':
            running = False
        else:
            p = Player.Player('My_Heroine', 20, 100, 50, 50, 120)
            p4 = Enemy.Enemy('Enemy 4', 10, 10, 55, 30, 55)
        
    print('Powering down...')
    
    