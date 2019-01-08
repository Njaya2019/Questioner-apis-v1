from flask import Blueprint,request,jsonify
from models.meetups_model import meetups
from validators.validate_json import validate_json_values

"""""""Initialize a flask blueprint of meetups"""""""

meetups_blueprint=Blueprint("meetups",__name__)

"""""""An endpoint to create a meetup"""""""
@meetups_blueprint.route("/api/v1/admin/createmeetup", methods=["GET","POST"])
def createmeetup():
    meetup_title=request.json['meetup_title']
    meetup_descrip=request.json['meetup_description']
    location=request.json['location']
    """""""Check if json values are empty"""""""
    if not meetup_title or not meetup_descrip or not location:
        return jsonify({"message":"Please fill all the meet up information"}),422
    """""""Check if json values are valid"""""""
    if not validate_json_values.validate_json_string_value(meetup_title) or not validate_json_values.validate_json_string_value(meetup_descrip) or not validate_json_values.validate_json_string_value(location):
        return jsonify({"message":"Please provide valid data"}),400
    """""""If all checkouts well then create meetup"""""""
    meetup_obj=meetups(meetup_title,meetup_descrip,location)
    data_submited_successfully=meetup_obj.add_meetup()
    return jsonify({"message":data_submited_successfully}),201

    
    


