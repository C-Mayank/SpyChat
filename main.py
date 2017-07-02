#importing data from spy_details file
from spy_details import spy,friends,Spy,chatMessage

#importing steganography
from steganography.steganography import Steganography

#importing termcolor package
from termcolor import colored




# status list defined
status_messages = ["My name is Bond, James Bond", "Shaken, not stirred", "Keep the British end up, Stir"]

# Print the text 'Hello'
print "Hello"

# use of escape sequence(\character) to print apostrophe s using single quotes
print 'Let\'s get started'

# ask user whether he wants to continue as guest
question = "Would you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)" + "? "

# accepting user input
existing = raw_input(question)





#function to add status
def add_status(current_status_message):

    #define a variable for updated status message
    updated_status_message = None

    #check if the status is already set
    if spy.current_status_message != None:
        print "Your current status is %s \n" % (current_status_message)
    else:
        print "You don't have any status currently selected\n"

    default = raw_input("Would you like to select your current status from any of the older status messages(Y/N)? ")

    #check if user wants to add a new status
    if default.upper() == "N":
        new_status_message = raw_input("Enter a new status: ")

        #check if the new status is not empty
        if len(new_status_message) > 0:
            status_messages.append(new_status_message)
            updated_status_message=new_status_message

    #check if user wants to add an older status
    elif default.upper() == "Y":
        item_position = 1

        #displaying the messages
        for message in status_messages:
            print "%d. %s" % (item_position, message)
            item_position = item_position + 1

        #Select a message
        message_selection = int(raw_input("\n Choose from the above messages: "))
        if len(status_messages) >= message_selection:
            updated_status_message = status_messages[message_selection - 1]

    else:
        #Invalid choice
        print "The option you chose is invalid! Press either Y or N: "

    #check if the status message has been updated
    if updated_status_message:
        print "Your updated status is %s " % (colored(updated_status_message,"blue"))
    else:
        print "You did not update your status!!!"


    #return the updated status
    return updated_status_message





#function to send a message
def send_message():
    #select a friend
    friend_choice = select_friend()

    #select an image for steganography
    original_image = raw_input("Enter the name of the image: ")
    output_path = "output.jpg"

    #message to be hidden using steganography
    text = raw_input("What would you like to say? ")

    #hiding message using steganography
    Steganography.encode(original_image, output_path, text)

    #check if secret text left empty
    if text != "":
        new_chat = chatMessage(text,True)
        friends[friend_choice].chats.append(new_chat)
        print "\nYour secret message has been created and ready for use!"
        #appending messages to a text file
        file = open("message.txt", "a")
        file.write(text)
        file.write(",")
        file.close()
    else:
        print "\nIt seems you didn\'t enter the secret message. Please try again!!!"





#function to read a secret message
def read_message():
    #choose the sender
    sender = select_friend()

    #decode the secret message using an image
    output_path = raw_input("What is the name of the output file? ")
    secret_text = Steganography.decode(output_path)
    print secret_text

    #if spy sends any SOS message
    if secret_text == "SOS" or secret_text =="SAVE ME" or secret_text == "HELP ME":
       print "The spy is in a trouble"
    else:
        new_chat = chatMessage(secret_text,False)
        friends[sender].chats.append(new_chat)
        #displaying the secret text
        print "Your decoded secret message is " + colored(secret_text,"blue")

    #reading messages from the file
    file = open("message.txt","r")
    str = file.read()
    print "Messages stored in file are: %s" % colored(str,"blue")




#funtion defined to add a friend
def add_friend():
    #New friend
    new_friend = Spy("", "", 0, 0.0)

    #Enter the details
    new_friend.name = raw_input("Please enter your friend's name: ")
    new_friend.salutation = raw_input("Is he a mister or miss? ")
    new_friend.name = new_friend.salutation + new_friend.name
    new_friend.age = raw_input("Please enter your friend's age: ")
    new_friend.age = int(new_friend.age)
    new_friend.rating =raw_input("Please enter your friend's rating: ")
    new_friend.rating = float(new_friend.rating)

    #Add a friend
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        #add a new friend in the list of friends
        friends.append(new_friend)
        print "Friend Added !!! "
    else:
        print "Sorry! Invalid Entry. We cannot add spy with the details you fed "


    #number of friends
    return len(friends)





def select_friend():
    #initialize the list number
    item_number = 0

    #display list of friends
    for friend in friends:
        #print the friends
        print "%d. %s aged %d with rating %.2f is online" % (item_number + 1, colored(friend.name,"red"), friend.age, friend.rating)
        item_number = item_number + 1

    #select a friend using index
    friend_choice = raw_input("Choose from your friends: ")
    friend_choice_position = int(friend_choice) - 1

    #friend position in list
    return friend_choice_position





#function to read chat history
def read_chat_history():
    #select a friend
    friend_selected = select_friend()

    #iterate friends chat
    for chat in friends[friend_selected].chats:
        if chat.sent_by_me:
            print "[%s] %s said: %s" % (colored(chat.time.strftime("%d,%B,%Y"),"blue"), colored(friends[friend_selected].name,"red"), chat.message)
        else:
            print "[%s] %s said: %s" % (colored(chat.time.strftime("%d,%B,%Y"),"blue"), colored(friends[friend_selected].name,"red"), chat.message)





# function defined for starting the chat
def start_chat(spy):
    file = open("message.txt","w")
    file.close()

    #no current message
    current_status_message = None

    # concatenating salutation with the spy name & update spy name
    spy.name = spy.salutation + " " + spy.name

    #check for valid age
    if spy.age > 12 and spy.age < 50:
        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and of rating: " +str(spy.rating)
        show_menu = True

        #show menu
        while show_menu:
            #show menu choices
            menu_choices = "\nWhat do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read chats from an user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            #check if menu choice is valid
            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
                #set status
                if menu_choice == 1:
                    current_status_message = add_status(current_status_message)
                #add friend
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print "You have %d friends " % (number_of_friends)
                #send message
                elif menu_choice == 3:
                    send_message()
                #read message
                elif menu_choice == 4:
                    read_message()
                #read chat history
                elif menu_choice == 5:
                    read_chat_history()
                #hide the menu
                else:
                    show_menu = False
    else:
        #Invalid age
        print "Sorry you are not of correct age to be a spy"

#check if user wants to continue with the default spy
if existing.upper() == "Y":
    #start the chat
    start_chat(spy)
else:
    #create an object for Spy class
    spy = Spy("","",0,0.0)

    # request the user for spy name
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    # check if spy name is valid or not
    if len(spy.name) > 0:
        # welcome the spy with name
        print "Welcome " + spy.name + ". Glad to have you back with us."

        # request the user for appropriate salutation
        spy.salutation = raw_input("Should I call you Mister or Miss?: ")

        # greet the spy with the name along with salutation
        print "Alright " + spy.name + ". I would like to know a little bit more about you before we proceed..."

        # ask spy age from the user
        spy.age = raw_input("Enter your age: ")

        # convert spy age into integer datatype
        spy.age = int(spy.age)

        # ask the user for spy rating
        spy.rating = raw_input("Enter your spy rating: ")

        # convert the spy rating into float datatype
        spy.rating = float(spy.rating)

        # spy comes online
        spy.is_online = True

        #start the chat
        start_chat(spy)
    else:
        #Invalid spy name
        print "A spy needs to have a valid name. Please try again "
