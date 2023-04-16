def new_line():

    print('.')

def three_lines():
    # Calls new line three times resulting in 3 lines being printed
    new_line()

    new_line()

    new_line()
    
def nine_lines():
    # Calls the three lines function three times to result in 9 lines being printed
    three_lines()
    
    three_lines()
    
    three_lines()
    
def clear_screen():
    # Calls the appropriate functions to print 25 lines
    nine_lines()
    
    nine_lines()
    
    three_lines()
    
    three_lines()
    
    new_line()
    
print('Calling nine_lines()')
nine_lines()
print('Calling clear_screen()')
clear_screen()