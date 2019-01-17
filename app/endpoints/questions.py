from flask import Blueprint, request,jsonify
from models.questions_model import questionsmodel
from validators.validate_json import validate_json_values
from models.questions_model import questionsmodel

questions_blueprint = Blueprint("questions",__name__)        #'Initialize a flask blueprint for questions'

@questions_blueprint.route("/api/v1/questions", methods=["POST"])
def createquestion():
    """
        An endpoint to ask a question
    """
    json_question_dict = request.get_json()
    question_keys_list =  ['title','body','userid','meetupid']
    if not all(json_key in json_question_dict for json_key in question_keys_list):    
        return jsonify({
            "status" : 400,
            "error" : "Please provide title, body, userid or meetupid to post a question"
            }),400

    question_title = json_question_dict['title'].strip()
    question_descrip = json_question_dict['body'].strip()
    user_id=json_question_dict['userid']
    meetup_id=json_question_dict['meetupid']

    if not question_title or not question_descrip or not user_id or not meetup_id:
        """
            Check if json values are empty
        """
        return jsonify({
            "status":400,
            "error":"Please fill both values for title and the body of the question to post a question"
            }), 400
    if not validate_json_values.validate_json_string_value(question_title) or not validate_json_values.validate_json_string_value(question_descrip) or not validate_json_values.validate_json_integer_value(meetup_id) or not validate_json_values.validate_json_integer_value(user_id):
        """
            Check if json values are valid
        """
        return jsonify({
            "status":400,
            "error":"The title and the body of the question must be strings.userid and meetupid must be integers"
            }), 400
    """
        If all checkouts well then ask a question
    """
    questionsmodel_obj=questionsmodel(question_title,question_descrip,user_id,meetup_id)
    question_asked=questionsmodel_obj.ask_question()
    if type(question_asked)!=dict:
        return jsonify({
            "status":404,
            "error":"You are posting a question on a meetup that doesn't exist"
            }), 404
    else:     
        return jsonify({
            "status":201,
            "data":{
                "meetupid":question_asked["meetupid"],
                "userid":question_asked["userid"],
                "title":question_asked["title"],
                "body":question_asked["body"]}
            }),201

@questions_blueprint.route("/api/v1/questions/<int:question_id>/upvote", methods=["PATCH"])
def upvote(question_id):
    """
        An endpoint to upvote a question and raises an error 
        if question doesn't exist
    """
    upvoted_question=questionsmodel.up_vote_question(question_id)
    if type(upvoted_question)==dict:
        return jsonify({
            'status':200,
            'data':upvoted_question
            }), 200
    return jsonify({
        "status":404,
        'error':upvoted_question
        }),404

@questions_blueprint.route("/api/v1/questions/<int:question_id>/downvote", methods=["PATCH"])
def downvote(question_id):
    """
        An endpoint to downvote a question
         and raises an error if question doesn't exist
    """
    downvoted_question=questionsmodel.down_vote_question(question_id)
    if type(downvoted_question)==dict:
        return jsonify({
                'status':200,
                'data':downvoted_question
                }), 200
    return jsonify({
        "status":404,
        'error':downvoted_question
        }),404