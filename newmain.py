from person import Person
import pickle
try:
   with open ('personSave.pickle', 'rb') as save:
      people = pickle.load(save)
except FileNotFoundError as e:
    people = []
    print ('file not gound' + str(e) + 'when closed, a new file is saved.')

def print_people():
    '''Iterates through the people list and prints out details'''
    for person in people:
     print('{0} {1} is {2} years old' .format(person.firstname, person.surname, person.age))
     return({0}, {1}, {2})
def create_person():
    ''' has the user create a person and adds the list'''
    firstname = input("please enter your firstname")
    surname = input("please enter your surname")
    dob = input("please enter your date of birth in the form of MMM DD YYY")
    new_ppl = Person(firstname, surname, dob)
    people.append(new_ppl)
    return new_ppl
def Closing_File():
    '''write the actual pickle file'''
    with open('personSave.picke', 'wb') as save:
       pickle.dump(people, save, protocol = pickle.HIGHEST_PROTOCOL)



