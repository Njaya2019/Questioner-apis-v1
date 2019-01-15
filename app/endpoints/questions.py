from flask import Blueprint,request,jsonify
from models.questions_model import questionsmodel
from validators.validate_json import validate_json_values
from models.questions_model import questionsmodel

questions_blueprint=Blueprint("questions",__name__)        #Initialize a flask blueprint for questions

@questions_blueprint.route("/api/v1/user/createquestion", methods=["POST"])
def createquestion():
    """An endpoint to ask a question
    """
    question_title=request.json['question_title'].strip()
    question_descrip=request.json['qusetion_description'].strip()
    user_id=request.json['user_id']
    meetup_id=request.json['meetup_id']
    if not question_title or not question_descrip or not user_id or not meetup_id:
        """Check if json values are empty
        """
        return jsonify({
            "status":400,
            "error":"Please fill all the question information"
            }), 400
    if not validate_json_values.validate_json_string_value(question_title) or not validate_json_values.validate_json_string_value(question_descrip) or not validate_json_values.validate_json_integer_value(meetup_id) or not validate_json_values.validate_json_integer_value(user_id):
        """Check if json values are valid"""
        return jsonify({"status":400,"error":"Please provide valid data"}), 400
    """
    If all checkouts well then ask question
    """
    questionsmodel_obj=questionsmodel(question_title,question_descrip,user_id,meetup_id)
    question_asked=questionsmodel_obj.ask_question()
    return jsonify({
        "status":201,
        "data":{
            "question_id":question_asked["question_id"],
            "question_title":question_asked["question_title"],
            "question_description":question_asked["question_description"]}
        }),201

@questions_blueprint.route("/api/v1/user/question/<int:question_id>/upvote", methods=["PATCH"])
def upvote(question_id):
    """An endpoint to upvote a question and raises an error
         if question doesn't exist
    """
    upvoted_question=questionsmodel.up_vote_question(question_id)
    if type(upvoted_question)==dict:
        return jsonify({
            'status':200,
            'data':upvoted_question
            }), 200
    return jsonify({'error':upvoted_question}),403

@questions_blueprint.route("/api/v1/user/question/<int:question_id>/downvote", methods=["PATCH"])
def downvote(question_id):
    """An endpoint to downvote a question
         and raises an error if question doesn't exist
    """
    downvoted_question=questionsmodel.down_vote_question(question_id)
    if type(downvoted_question)==dict:
        return jsonify({
                'status':200,
                'data':downvoted_question
                }), 200
    return jsonify({'error':downvoted_question}),403