from flask import Blueprint,request,jsonify
from validators.validate_json import validate_json_values
from models.user_model import users_model
import jwt, datetime

#Initialize a flask blueprint of users authentication endpoints

userauth_blueprint=Blueprint("users",__name__)

@userauth_blueprint.route("/api/v1/signup", methods=["POST"])
def register_user():
    
    """
        An endpoint to register a user.
        First it gets the values from the user
    """
    user_json_dict=request.get_json()  

    user_keys_list=[
        'firstname','lastname',
        'email','username',
        'isAdmin','phonenumber',
        'password','confirmpassword']

    if not all(json_key in user_json_dict for json_key in user_keys_list):    
        return jsonify({
            "status":400,
            "error_msg":"firstname, lastname,email,username,isAdmin,phonenumber,password or confirmpassword key is missing"
            }),400

    first_name=user_json_dict['firstname']
    last_name=user_json_dict['lastname']
    email=user_json_dict['email']
    username=user_json_dict['username']
    isAdmin=user_json_dict['isAdmin']
    phonenumber=user_json_dict['phonenumber']
    password=user_json_dict['password']
    confirm_pwd=user_json_dict['confirmpassword']
    
    if not validate_json_values.validate_json_email_value(email):
        """Check if the email is valid
        """
        return jsonify({
            "status":400,
            "error_msg":"The email provided is an invalid email. provide a valid email"
            }),400
    if not validate_json_values.validate_json_string_value(first_name) or not validate_json_values.validate_json_string_value(last_name) or not validate_json_values.validate_json_string_value(username) or not validate_json_values.validate_json_string_value(isAdmin) or not validate_json_values.validate_json_string_value(email):
        """
        Check if json values are valid
        """
        return jsonify({
            "status":400,
            "error_msg":"firstname, lastname,email,username,isAdmin,phonenumber,password and confirmpassword valuesa must be all strings"
            }),400
    else:
        """
        Remove white spaces at the begining
        and end of the string.
        """
        first_name=first_name.strip()
        last_name=last_name.strip()
        email=email.strip()
        username=username.strip()
        email=email.strip()
        isAdmin=isAdmin.strip()
        phonenumber=phonenumber.strip()
        if not first_name or not username or not last_name or not email or not isAdmin or not password or not confirm_pwd:
            """
                Check if json values are empty
            """
            return jsonify({
                "status":400,
                "error_msg":"firstname, lastname,email,username,isAdmin,phonenumber,password and confirmpassword must have values"
                }),400
        """
            If all checkouts well then add user
        """
        user_obj=users_model(first_name,last_name,email,username,isAdmin,phonenumber,password,confirm_pwd)
        user_data=user_obj.register_user()
        if type(user_data)!=dict:
            return jsonify({
                "status":409,
                "error_msg":user_data
                }),409
        return jsonify({"status":201,"data":user_data}),201


@userauth_blueprint.route("/api/v1/login", methods=["POST"])
def login_user():
    
    """
        An endpoint to login user. 
        It gets credentials from the user
    """
    login_json_dict=request.get_json()  

    login_keys_list=['email','password',]

    if not all(json_key in login_json_dict for json_key in login_keys_list):    
        return jsonify({
            "status":400,
            "error_msg":"email or password key is missing. please provide it"
            }),400

    email=login_json_dict['email']
    password=login_json_dict['password']

    email=email.strip()
    password=password.strip()
    if not validate_json_values.validate_json_email_value(email) and email:
        """
            Check if the email is valid
        """
        return jsonify({
            "status":400,
            "error_msg":"The email provided is not a valid email. please provide a valid email"
            }),400
    if not email or not password:
        """
            Check if email and password values are empty
        """
        return jsonify({
            "status":400,
            "error_msg":"Both email and password values are required to login"
            }),400
    """
        If all checks out get the user from users list
    """
    current_user=users_model.signin_user(email,password)
    if type(current_user)!=dict:
        """
            if email wasn't found or the password is incorrrect
        """
        return jsonify({
            "status":401,
            "error_msg":current_user
            }), 401
    else:
        """
            If the email and password are correct then generate token
        """
        token=jwt.encode({"id":current_user["id"],"exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},'secret',algorithm='HS256')
        return jsonify({
            'token':token.decode('UTF-8'),
            "data":{
                "firstname":current_user["firstname"],
                "username":current_user["username"],
                "isAdmin":current_user["isAdmin"]
                }}), 200