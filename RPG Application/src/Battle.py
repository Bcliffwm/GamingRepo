from src.Character import Character

def combat(a: Character,  b : Character):
    turn_count = 1
    while not(a.is_dead() and b.is_dead()):
        a.attack_other(b)
        if(b.is_dead()):
            print('Character: ' + b.name + 'is dead')
            break
        
        b.attack_other(a)
        if(a.is_dead()):
            print('Character: ' + a.name + 'is dead')
            break
        
        turn_count += 1

    print(turn_count)