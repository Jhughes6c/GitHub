from newmain import Closing_File, print_people, create_person

def menu():
    '''' creates a list of options for the user'''
    print("welcome to the menu!")
    print("please select one of the following:")
    print("1 = create new person")
    print("2 print the person list")
    print("3 = exit the menu")
    
    menu = input("what do you want to do?")
    if menu == '1':
        create_person()
        Closing_File()
        print_people()
    elif menu == '2':
        print_people()
        Closing_File()
    elif menu == '3':
        print("saving...")
        print("goodbye for now")
        Closing_File()
        exit()
if __name__ == '__main__':
    while True:
        menu()


