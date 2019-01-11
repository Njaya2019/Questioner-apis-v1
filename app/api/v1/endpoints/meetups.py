from flask import Blueprint,request,jsonify
from app.api.v1.models.meetups_model import meetups,meetups_list
from app.api.v1.validators.validate_json import validate_json_values

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
        return jsonify({"status":422,"error_msg":"Please fill all the meet up information"}),422
    """""""Check if json values are valid"""""""
    if not validate_json_values.validate_json_string_value(meetup_title) or not validate_json_values.validate_json_string_value(meetup_descrip) or not validate_json_values.validate_json_string_value(location):
        return jsonify({"status":400,"error_msg":"Please provide valid data"}),400
    """""""If all checkouts well then create meetup"""""""
    meetup_obj=meetups(meetup_title,meetup_descrip,location)
    meetup_data=meetup_obj.add_meetup()
    return jsonify({"status":201,"meeeup_created":meetup_data}),201

    
"""""""An endpoint to get a specifi meetup record"""""""
@meetups_blueprint.route("/api/v1/admin/meetups/<int:meetup_id>", methods=["GET","POST"])
def get_a_meetup_record(meetup_id):
    meetup_record=meetups.get_a_meetup(meetup_id)
    """""""if a meetup record was found it's a dictionary else raise an error"""""""
    if type(meetup_record)==dict:
        return jsonify({"status":200,"meetup_record":meetup_record}), 200
    return jsonify({"status":404,"error_msg":meetup_record}),404

"""""""An endpoint to get all meetups record"""""""
@meetups_blueprint.route("/api/v1/admin/meetups", methods=["GET","POST"])
def get_all_meetups():
    if not meetups_list:
        return jsonify({"status":404,"error_msg":"There are no meetups yet"}),404   
    """""""Uses global list imported from meetups_model that holds all meetups"""""""
    return jsonify({"Meetups":meetups_list}), 200