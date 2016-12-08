#mian.py
from person import Person

people = []

def main():
    ''' makes a user input the persons code'''
    p1 = Person(firstname, surname, dob)
    people.append(p1)

def print_people():
    '''Iterates through the people list and prints out details'''

    for person in people:
     print('{0} {1} is {2} years old' .format(person.firstname, person.surname, person.age))
def create_person():
    ''' has the user create a person and adds the list'''
    firstname = input("please enter your firstname")
    surname = input("please enter your surname")
    dob = input("please enter your date of birth in the form of MMM DD YYY")
    return (firstname, surname, dob)
    
def menu():
    '''' creates a list of options for the user'''
    answer = input(" select your option\n1 = add person\n2 = see list of users\n3 = exit program\nwhat would you like to do?")
    while answer:
        if answer == ('1'):
           main.firstname, surname, dob = create_person()
           print_people()
           a = input("add another?")
           if a == 'no':
            answer = False
        elif answer == ('2'):
           print = (print_people())
if __name__ == '__main__':
  while True:
   menu()
 
    
    #PLEASE HELP, THIS CODE IS NOT WORKING
   #i cannae print becos its stupid
    
    
    







