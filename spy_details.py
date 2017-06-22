#importing datetime package
from datetime import datetime

#creating a class for a spy
class Spy:

    #constructor of spy class
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


#creating a default spy user
spy = Spy("Bond","Mr.",25,4.7)


#creating spy friends
friend_one = Spy("Raja","Mr.",27,4.9)
friend_two = Spy("Mata Hari","Mrs.",20,5.0)
friend_three = Spy("Noddy","Dr.",4.4,38)

#assigning friends to friends list
friends = [friend_one, friend_two, friend_three]


#creating a class for chat message
class chatMessage:

    #constructor of chat message class
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

