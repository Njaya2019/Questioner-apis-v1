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
        return meetup_dict
    """""""A class method to check if meetups list is empty and if the meetup doesn't exist"""""""
    @classmethod
    def err_message(cls,meetup_id=None):
        if meetup_id>len(meetups_list):
            return "The meetup record wasn\'t found"
        if not meetups_list:
            return "The meetup record wasn\'t found"
        return 0
    """""""A class method to get a specific meetup"""""""    
    @classmethod
    def get_a_meetup(cls,meetup_id):
        """""""Checks if meetup id is out of bounds in meetup list hence record wasn't found"""""""
        msg=cls.err_message(meetup_id)
        if msg !=0:
            return msg
        meetup_record=meetups_list[meetup_id-1]
        return {"meetup_id":meetup_record["meetup_id"],"meetup_title":meetup_record["meetup_title"],"meetup_description":meetup_record["meetup_description"],"location":meetup_record["location"],"date_created":meetup_record["date_created"]}
