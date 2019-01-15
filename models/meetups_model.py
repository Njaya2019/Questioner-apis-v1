import datetime

meetups_list=[]        #Initialized a global list to hold all meetups

class meetups():
    
    """
    A class model to store meetups data
    """

    def __init__(self,meetup_title,meetup_description,location):
        """
        Create instance variables of class meetups
        """
        self.meetup_title=meetup_title
        self.meetup_description=meetup_description
        self.location=location
        now=datetime.datetime.now()
        now=now.strftime("%Y-%m-%d %H:%M")
        self.date_created=now
        self.meetup_id=len(meetups_list)+1   
    
    def add_meetup(self):
        """
        Create a meetup and holds each meetup on a dictionary
        """
        meetup_dict={
            "id":self.meetup_id,
            "topic":self.meetup_title,
            "description":self.meetup_description,
            "location":self.location,"createdOn":self.date_created
            }
        meetups_list.append(meetup_dict)
        return meetup_dict

    @classmethod
    def err_message(cls,meetup_id=None):
        """A class method to check if meetups list is
             empty and if the meetup doesn't exist
        """
        if meetup_id>len(meetups_list):
            return "The meetup record wasn\'t found"
        if not meetups_list:
            return "The meetup record wasn\'t found"
        return 0 

    @classmethod
    def get_a_meetup(cls,meetup_id):
        """
        A class method to get a specific meetup
        """ 
        msg=cls.err_message(meetup_id)
        if msg !=0:
            """Checks if meetup id is out of bounds in
                 meetup list hence record wasn't found
            """
            return msg
        meetup_record=meetups_list[meetup_id-1]
        return {
            "id":meetup_record["id"],
            "topic":meetup_record["topic"],
            "description":meetup_record["description"],
            "location":meetup_record["location"],
            "createdOn":meetup_record["createdOn"]
            }