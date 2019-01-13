from flask import Blueprint,request,jsonify
from validators.validate_json import validate_json_values
from models.user_model import users_model

"""""""Initialize a flask blueprint of users authentication endpoints"""""""

userauth_blueprint=Blueprint("users",__name__)

"""""""An endpoint to register a user"""""""
@userauth_blueprint.route("/api/v1/registration", methods=["GET","POST"])
def register_user():
    """""""gets values from the user"""""""
    first_name=request.json['user_firstname']
    second_name=request.json['user_secondname']
    gender=request.json['user_gender']
    email=request.json['user_email']
    account_type=request.json['account_type']
    password=request.json['password']
    confirm_pwd=request.json['confirm_password']

    """""""Check if the email is valid"""""""
    if not validate_json_values.validate_json_email_value(email):
        return jsonify({"status":400,"error_msg":"Please provide a valid email"}),400
    """""""Check if json values are empty"""""""
    if not first_name or not second_name or not gender or not email or not password or not confirm_pwd:
        return jsonify({"status":400,"error_msg":"All user's information is required to register"}),422
    """""""Check if json values are valid"""""""
    if not validate_json_values.validate_json_string_value(first_name) or not validate_json_values.validate_json_string_value(second_name) or not validate_json_values.validate_json_string_value(email):
        return jsonify({"status":400,"error_msg":"Please provide user valid values"}),400
    """""""If all checkouts well then add user"""""""
    user_obj=users_model(first_name,second_name,gender,email,account_type,password,confirm_pwd)
    user_data=user_obj.register_user()
    if type(user_data)!=dict:
        return jsonify({"status":409,"error_msg":user_data}),409
    return jsonify({"status":201,"user":user_data}),201