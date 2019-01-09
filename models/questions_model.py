import datetime

"""""""Initialized a global list to hold all questions"""""""
questions_list=[]

"""""""A class model of questions"""""""
class questionsmodel():
    """""""Create instance variables of class questionsmodel"""""""
    def __init__(self,question_title,question_description,user_id,meetup_id):
        self.question_title=question_title
        self.question_description=question_description
        """""""The date and time the question was created""""""" 
        now=datetime.datetime.now()
        now=now.strftime("%Y-%m-%d %H:%M")
        self.user_id=user_id
        self.meetup_id=meetup_id
        self.date_asked=now
        self.question_id=len(questions_list)+1
    """""""An intance method to ask a question and returnit's id,title and description"""""""
    def ask_question(self):
        question_dict={"question_id":self.question_id,"question_title":self.question_title,"question_description":self.question_description,"user_id":self.user_id,"meetup_id":self.meetup_id,"date_created":self.date_asked}
        questions_list.append(question_dict)
        return {"question_id":self.question_id,"question_title":self.question_title,"question_description":self.question_description}