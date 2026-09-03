def display_menu():
    print("------Menu------")
    print("1-Counter ")
    print("2-Even_Odd ")
    print("3-Max ")
    print("4-Quiz Game ")
    print("5-Simple calculator ")
    print("6-Exit")

def get_valid_choice():
    while True :
        display_menu()
        try:
            choice = int(input('Enter your choice : '))
            return choice
        except ValueError:
            print("error!")


# counter


def counter():         
    phrase = input("please enter the phrase: ")
    letters,spaces,numbers = 0 , 0 , 0

    for element in phrase :
        if element == ' ':
            spaces += 1
        elif element.isdigit():
            numbers += 1
        else:
            letters += 1

    print(f"Letters: {letters}, Spaces: {spaces}, Numbers: {numbers}")
    return

def number_validation():

    while True :
        try :
            number = int(input('Enter the number : '))
            return number
        except ValueError:
            print('try again !! ')          


#even_odd


def even_odd():              
    number = number_validation()
    if number % 2 == 0:
        print(f"{number} is even .")
    else :
        print(f"{number} is odd .")


#maximum

def get_lenght():
    while True : 
        try :
            lenght = int(input('Enter the lenght : '))
            if lenght > 0 :
                return lenght
        except ValueError : 
            print("error!")

def remplissage_max_liste():
    lenght = get_lenght()
    liste = []
    for _ in range(lenght):
        number = number_validation()
        liste.append(number)

    print(f"Liste : {liste} ")

    print(f"The maximum is : {max(liste)} ")


#Quiz game 

def quiz_game():
    quiz = {
    "What is the capital of Morocco?": "Rabat",
    "What is 5 + 5?": "10",
    "Which programming language are we learning?": "Python"
     }
    score = 0
    for key,value in quiz.items():
        print(f"{key}")
        answer = input(" : ")
        if answer.upper() == value.upper():
           print("correct answer.")
           score += 1
        else :
           print("wrong answer")

    print(f"your final score is {score}")

#Simple Calculatoe

def display_menu0():
    print("choose the operation ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
def number_validation():
    while True :
        try:
            number = int(input('Enter the number : '))
            return number
        except ValueError :
            print("Error , Try again .")
def simple_calculator():

 while True :
    display_menu0()
    choice = number_validation()
    if choice == 5 :
        break
    a =  number_validation()
    b  =  number_validation()   
    
    if choice == 1 :
        print(f'{a} + {b} = {a + b}')
    elif choice == 2:
        print(f'{a} - {b} = {a - b}')
    elif choice == 3:
        print(f'{a} * {b} = {a * b}')
    elif choice == 4:
        if b == 0:
            print("Error ! ")
        else:
            print(f'{a} / {b} = {a / b}')
        
    else :
        print('Invalid Choice !! ')



    