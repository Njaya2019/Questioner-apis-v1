import datetime

"""""""Initialized a global list to hold all questions"""""""
questions_list=[]
"""""""""makes votes variable a global variable"""""""""
votes=0
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
        question_dict={"question_id":self.question_id,"question_title":self.question_title,"question_description":self.question_description,"user_id":self.user_id,"meetup_id":self.meetup_id,"date_created":self.date_asked,"votes":votes}
        questions_list.append(question_dict)
        return {"question_id":self.question_id,"question_title":self.question_title,"question_description":self.question_description}
    """""""A class method to vote upvote on a question by increamenting votes variable by 1"""""""
    @classmethod
    def up_vote_question(cls,question_id):
        if question_id > len(questions_list):
            return "Forbidden. The question doesn\'t exist"
        if not questions_list:
            return "Forbidden. The question doesn\'t exist"
        """""""gets the question and upvotes it"""""""
        global votes
        votes=votes+1
        question_upvote=questions_list[question_id-1]
        question_upvote.update({"votes":votes})
        return {"meetup_id":question_upvote['meetup_id'],"question_title":question_upvote['question_title'],"question_description":question_upvote['question_description'],"votes":question_upvote['votes']}
    """""""A class method to down vote on a question by decreamenting votes variable by 1"""""""
    @classmethod
    def down_vote_question(cls,question_id):
        if question_id > len(questions_list):
            return "Forbidden. The question doesn\'t exist"
        if not questions_list:
            return "Forbidden. The question doesn\'t exist"
        """""""gets the question and downvotes it"""""""
        global votes
        votes=votes-1
        question_downvote=questions_list[question_id-1]
        question_downvote.update({"votes":votes})
        return {"meetup_id":question_downvote['meetup_id'],"question_title":question_downvote['question_title'],"question_description":question_downvote['question_description'],"votes":question_downvote['votes']}
