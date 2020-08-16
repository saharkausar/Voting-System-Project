#   SCRIPT: votingSystem.py
#   AUTHOR: Sahar Kausar
#   CONTACT: saharkausar@gmail.com
#
#   Anita Borg - Python Certification Course
#
#   DESCRIPTION: A Python-Based (Bonus and Final) Project Through the Anita Borg - Python Certification Course!
#                The objective of the program is to provide a national voting system for the citizens of a country.

import PySimpleGUI as sg

##-----BUTTON SETTINGS----------------------------------##
layout1_button_spec: dict = {'size':(18, 1), 'font':('Franklin Gothic Book', 22), 'button_color':("White","#bdd3de")}
layout2_button_spec: dict = {'size':(13, 1), 'font':('Franklin Gothic Book', 12), 'button_color':("White","#bdd3de")}

##-----VARIOUS LAYOUTS---------------------------------##
layout1: list = [
    [sg.Text('National Voting System', size=(50,1), justification='center', background_color="#debdc2",
        text_color='White', font=('Franklin Gothic Book', 14, 'bold'))],
    [sg.Button('Login to Cast Vote', **layout1_button_spec)],
    [sg.Button('See Voting Results', **layout1_button_spec)],
    [sg.Button('Exit Program', **layout1_button_spec),]
]

layout2 = [
    [sg.Text('Example Name and Voter ID Input (First Name and Integer Number): Bob101')],
    [sg.Text('Enter Your Name and Voter ID:'), sg.InputText()],
    [sg.Button('Enter Voter ID', **layout2_button_spec), sg.Button('Main Menu', **layout2_button_spec)]
]


layout3 = [
    [sg.Text('Hint - The Password is: PassVoteNow')],
    [sg.Text('Please enter the password:'), sg.InputText()],
    [sg.Button('Enter Password', **layout2_button_spec), sg.Button('Back', **layout2_button_spec)]
]

layout4 = [
    [sg.Text('Please Vote for a Party:')],
    [sg.Button('Believers', **layout2_button_spec), sg.Button('Dreamers', **layout2_button_spec)],
]

##-----WINDOW AND LAYOUT---------------------------------##
layout = [[sg.Column(layout1, key='-COL1-', element_justification='center'), sg.Column(layout2, visible=False, key='-COL2-', element_justification='center'), sg.Column(layout3, visible=False, key='-COL3-', element_justification='center'), sg.Column(layout4, visible=False, key='-COL4-', element_justification='center')]]
window: object = sg.Window('National Voting System', layout=layout, background_color="#debdc2", size=(500, 280), element_justification='center')

##-----HELPER FUNCTIONS BASED ON CLICK EVENTS---------------------------------##

#Defines the initial voting count for the election parties
Believers = 0
Dreamers  = 0

#Function that allows a valid user to vote!
def voteNow():

    #Launches the voting layout
    global layout
    layout = 2
    window[f'-COL{layout}-'].update(visible=False)
    layout = layout + 2
    window[f'-COL{layout}-'].update(visible=True)

    while True:
        event, values = window.read()

        #If the user selects the 'Believers' party and votes for them
        if event == 'Believers':
            #Then we increment the vote count of that party by 1
            global Believers
            Believers = Believers + 1

            #Displays the prompt that the vote was registered
            print("Your vote for the Believers party has been registered. Thank you for voting!")
            print(Believers)

            #Returns the user to the main menu
            window[f'-COL{layout}-'].update(visible=False)
            layout = layout - 3
            window[f'-COL{layout}-'].update(visible=True)
            return Believers
            break

        #If the user selects the 'Dreamers' party and votes for them
        elif event == 'Dreamers':
            #Then we increment the vote count of that party by 1
            global Dreamers
            Dreamers = Dreamers + 1

            #Displays the prompt that the vote was registered
            print("Your vote for the Dreamers party has been registered. Thank you for voting!")
            print(Dreamers)

            #Returns the user to the main menu
            window[f'-COL{layout}-'].update(visible=False)
            layout = layout - 3
            window[f'-COL{layout}-'].update(visible=True)
            return Dreamers
            break

#Class that creates objects of each designated voter
class Voter:
  def __init__(self, name, voted):
    self.name = name
    self.voted = voted

v1 = Voter("Bob101", False)
v2 = Voter("Sally102", False)
v3 = Voter("Joe103", False)

#Function that checks whether the user's voter ID is valid or invalid
def checkVoterID(voterID):

    #List of individuals that are registered (valid voters)
    validVoters = [v1, v2, v3]
    validID = False

    #For each value in our validVoters list
    for x in validVoters:
        #If the input name is equal to one of the validVoters object's name
        if x.name == voterID:
            #Then we create a new object within the local scope to check for equivalency later
            currentVoter = Voter(x.name, x.voted)
            #Indicates whether or not the input matched one of the objects
            validID = True

    #If the input given by the user is not registered in our validVoters object list
    if validID == False:
        #Then we return a message listing it as invalid credentials and redirects the user to the initial page menu.
        global layout, Column
        layout = 2
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout - 1
        window[f'-COL{layout}-'].update(visible=True)

        print("Invalid Voter ID! Please return to the main menu and enter a registered voter ID!")

    elif validID == True:
        #Then we know they are a valid registered user - Let's check if they have voted or not!

        #If the result of the voter is True (the voter has already voted)
        if currentVoter.voted == True:
            #Then we let the user know that they have voted and redirect them to the main menu
            print("You have already voted - Thank you! Please return to the main menu!")

            window[f'-COL{layout}-'].update(visible=False)
            layout = layout - 1
            window[f'-COL{layout}-'].update(visible=True)

        #If the result is False, then we know they have yet to vote - Let's vote!
        elif currentVoter.voted == False:

            #Bob101
            if voterID == "Bob101":
                #Then we set Bob's voted value to True (Bob has voted)
                v1.voted = True

                #Redirects the user to the voting page to vote!
                voteNow()

            #Sally102
            elif voterID == "Sally102":
                #Then we set Sally's voted value to True (Sally has voted)
                v2.voted = True

                #Redirects the user to the voting page to vote!
                voteNow()

            #Joe103
            elif voterID == "Joe103":
                #Then we set Joe's voted value to True (Joe has voted)
                v3.voted = True

                #Redirects the user to the voting page to vote!
                voteNow()

#Function that checks the password of the user and displays the results of the election
def checkPassword(password):
    #Password stored in the registration system
    passcode = "PassVoteNow"

    #If the password input by the user does not match the stored passcode
    if password != passcode:
        #Then we display a message that the password does not match the passcode and redirect the user to the initial page menu.
        print("You have entered an incorrect password. Please return to the main page!")

        global layout, Column
        layout = 3
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout - 2
        window[f'-COL{layout}-'].update(visible=True)

    #If the password input by the user does match the stored passcode
    else:
        #Displays the election results
        print("Believers Party Vote Count:", Believers)
        print("Dreamers Party Vote Count:", Dreamers)

        #Displays the winning Party
        if Believers > Dreamers:
            print("The Believers party is currently winning the election!")
        elif Dreamers > Believers:
            print("The Dreamers party is currently winning the election!")
        elif Believers == 0 or Dreamers == 0:
            print("There are currently no votes in this election! Please remember to cast a vote if you have a valid voter ID!")

##-----MAIN EVENT LOOP---------------------------------##
layout = 1  # The currently visible layout
while True:
    event, values = window.read()
    if event in (None, 'Exit Program'):
        break
    if event == "Login to Cast Vote":
        window[f'-COL{layout}-'].update(visible=False)
        #layout = layout + 1 if layout < 3 else 1
        layout = layout + 1
        window[f'-COL{layout}-'].update(visible=True)
    elif event == "Enter Voter ID":
        checkVoterID(values[0])
    elif event == "Main Menu":
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout - 1
        window[f'-COL{layout}-'].update(visible=True)
    elif event == "See Voting Results":
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout + 2
        window[f'-COL{layout}-'].update(visible=True)
    elif event == "Enter Password":
        checkPassword(values[1])
    elif event == "Back":
        window[f'-COL{layout}-'].update(visible=False)
        layout = layout - 2
        window[f'-COL{layout}-'].update(visible=True)
window.close()
