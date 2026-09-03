from operations import  get_valid_choice , counter , remplissage_max_liste ,even_odd ,quiz_game ,simple_calculator




def main():
    while True:
        
        choice = get_valid_choice()
        if choice == 1 :
            counter()
        elif choice == 2:
            even_odd()
        elif choice == 3:
            remplissage_max_liste()
        elif choice == 4:
            quiz_game()
        elif choice == 5:
            simple_calculator()
        elif choice == 6:
            break   
        else :
            print("invalid choice")






main()
        


