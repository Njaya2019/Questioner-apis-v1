from models.meetups_model import meetups_list

rsvp_list=[]        #creates a rsvp list to store all rsvp response data

class rsvp_model():
    """
    This is a class that implements the storage of rsvp responses
    """
    def __init__(self,user_id,rsvp_response):
        """
        Initializes instance variables
        """
        self.user_id=user_id
        self.rsvp_response=rsvp_response
        self.rsvp_id=len(rsvp_list)+1
    def rsvp_response_method(self,meetup_id):
        """
        An instance method to create rsvp response
        """
        if meetup_id>len(meetups_list):
            return "The meetup no longer exists or doesn't exists"
        if not meetups_list:
            return "The meetup no longer exists or doesn't exists"
        rsvp_meetup=meetups_list[meetup_id-1]
        rsvp_meetup_topic=rsvp_meetup["meetup_title"]
        rsvp={
            "rsvp_id":self.rsvp_id,"meetup_id":meetup_id,
            "meetup_title":rsvp_meetup_topic,"user_id":self.user_id,
            "rsvp_response":self.rsvp_response
            }
        rsvp_list.append(rsvp)
        return rsvp
    