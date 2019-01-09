from flask import Blueprint,request,jsonify
from models.questions_model import questionsmodel
from validators.validate_json import validate_json_values
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
        """""""Check if json values are empty"""""""
        if not question_title or not question_descrip or not user_id or not meetup_id:
            return jsonify({"status":422,"error":"Please fill all the question information"}), 422
        """""""Check if json values are valid"""""""
        if not validate_json_values.validate_json_string_value(question_title) or not validate_json_values.validate_json_string_value(question_descrip) or not validate_json_values.validate_json_integer_value(meetup_id) or not validate_json_values.validate_json_integer_value(user_id):
            return jsonify({"status":400,"error":"Please provide valid data"}), 400
        """""""If all checkouts well then ask question"""""""
        questionsmodel_obj=questionsmodel(question_title,question_descrip,user_id,meetup_id)
        question_asked=questionsmodel_obj.ask_question()
        return jsonify({"question_id":question_asked["question_id"],"question_title":question_asked["question_title"],"question_description":question_asked["question_description"]}),201



