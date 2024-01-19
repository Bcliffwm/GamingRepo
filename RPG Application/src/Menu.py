def display_starting_screen():
    print("Welcome to the Python RPG!")
    
def display_menu():
    
    selection = ""
    while(selection == "" or selection != '1'):
        selection = input('Make a selection: \na) Play game\ns)Save Character\nq)Quit Game\n')
        if(selection.lower() == 'q' or selection.lower() == 'a'):
            return selection
    
    return selection