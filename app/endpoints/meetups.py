from flask import Blueprint,request,jsonify
from models.meetups_model import meetups,meetups_list
from models.rsvp_model import rsvp_model
from validators.validate_json import validate_json_values

meetups_blueprint=Blueprint("meetups",__name__)        #Initialize a flask blueprint of meetups


@meetups_blueprint.route("/api/v1/admin/meetups", methods=["POST"])
def createmeetup():
    
    """An endpoint to create a meetup
    """
    meetup_title=request.json['topic']
    meetup_descrip=request.json['description']
    location=request.json['location']

    if not validate_json_values.validate_json_string_value(meetup_title) or not validate_json_values.validate_json_string_value(meetup_descrip) or not validate_json_values.validate_json_string_value(location):
        """Check if json values are valid
        """
        return jsonify({
                "status":400,
                "error_msg":"Please provide valid data"
                }),400
    else:
        """
        Remove white spaces at the begining
        and end of the string.
        """
        meetup_descrip=meetup_descrip.strip()
        meetup_title=meetup_title.strip()
        location=location.strip()
        if not meetup_title or not meetup_descrip or not location:
            """Check if json values are empty
            """
            return jsonify({
                    "status":400,
                    "error_msg":"Please fill all the meet up information"
                    }),400
        """
        If all checkouts well then create meetup
        """
        meetup_obj=meetups(meetup_title,meetup_descrip,location)
        meetup_data=meetup_obj.add_meetup()
        return jsonify({"status":201,"data":meetup_data}),201

@meetups_blueprint.route("/api/v1/admin/meetups/<int:meetup_id>", methods=["GET"])
def get_a_meetup_record(meetup_id):
    
    """An endpoint to get a specifi meetup record
    """
    meetup_record=meetups.get_a_meetup(meetup_id)
    if type(meetup_record)==dict:
        """if a meetup record was found it's a dictionary return
             it else raise an error
        """
        return jsonify({
            "status":200,
            "data":meetup_record
            }), 200
    return jsonify({"status":404,"error_msg":meetup_record}),404

@meetups_blueprint.route("/api/v1/admin/meetups", methods=["GET"])
def get_all_meetups():
    
    """An endpoint to get all meetups 
    """

    if not meetups_list:
        return jsonify({
            "status":404,
            "error_msg":"There are no meetups yet"
            }),404   
    """Uses global list imported from 
        meetups_model that holds all meetups
    """
    return jsonify({'status':200,"data":meetups_list}), 200

@meetups_blueprint.route("/api/v1/user/meetups/<int:meetup_id>/rsvp", methods=["POST"])
def respond_rsvp(meetup_id):
    
    """An endpoint to respond to an RSVP
    """
    user_id=request.json["userid"]
    rsvp_user_response=request.json["RSVPresponse"].strip()
    rsvp_obj=rsvp_model(user_id,rsvp_user_response)
    user_response=rsvp_obj.rsvp_response_method(meetup_id)
    if type(user_response)!=dict:
        return jsonify({"status":404,"error_msg":user_response}),404
    return jsonify({
        "status":201,
        "data":{"status":user_response["RSVPresponse"],
                "topic":user_response["meetuptopic"],
                "meetupid":user_response["meetupid"]}
                }),201
