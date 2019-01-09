from flask import Blueprint,request,jsonify
from models.questions_model import questionsmodel

"""""""Initialize a flask blueprint for questions"""""""

questions_blueprint=Blueprint("questions",__name__)

"""""""An endpoint to ask a question"""""""
@questions_blueprint.route("/api/v1/user/createquestion", methods=["GET","POST"])
def createquestion():
    if request.method=="POST":
        question_title=request.json['question_title']
        question_descrip=request.json['qusetion_description']
        user_id=request.json['user_id']
        meetup_id=request.json['meetup_id']
        """""""If all checkouts well then ask question"""""""
        questionsmodel_obj=questionsmodel(question_title,question_descrip,user_id,meetup_id)
        question_asked=questionsmodel_obj.ask_question()
        return jsonify({"question_id":question_asked["question_id"],"question_title":question_asked["question_title"],"question_description":question_asked["question_description"]}),201



