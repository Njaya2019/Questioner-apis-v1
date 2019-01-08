import datetime

"""""""Initialized a global list to hold all meetups"""""""
meetups_list=[]

"""""""A class model to store meetups data"""""""
class meetups():
    """""""Create instance variables of class meetups"""""""

    def __init__(self,meetup_title,meetup_description,location):
        self.meetup_title=meetup_title
        self.meetup_description=meetup_description
        self.location=location
        now=datetime.datetime.now()
        now=now.strftime("%Y-%m-%d %H:%M")
        self.date_created=now
        self.meetup_id=len(meetups_list)+1
    """""""Create a meetup and holds each meetup on a dictionary"""""""
    def add_meetup(self):
        meetup_dict={"meetup_id":self.meetup_id,"meetup_title":self.meetup_title,"meetup_description":self.meetup_description,"location":self.location,"date_created":self.date_created}
        meetups_list.append(meetup_dict)
        return "congratulations you have created a meet up"