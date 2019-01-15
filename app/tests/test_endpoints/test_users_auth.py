import pytest, json
from application import create_app

@pytest.fixture
def cli_ent():
    """
    Creates a test client fixture to be used in several test cases
    """
    app=create_app()
    client=app.test_client()
    return client

class TestsUserRegistration():
    
    def test_register_user(self,cli_ent):
        """This instance method test for successful registration of users.
        This test if the enpoint registers a user and returns a user id,
        first name and second name.
        """
        response=cli_ent.post('/api/v1/registration',
            data=json.dumps(dict(
                firstname="Juma",secondname="Masha",
                othername="Karisa",email="jumamasha@gmail.com",
                username="Juma",isAdmin="True",
                phonenumber="0727645367",password="1234",
                confirmpassword="1234"
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==201
        assert 1==data["data"]["id"]
        assert "Juma"==data["data"]["firstname"]
        assert "Masha"==data["data"]["secondname"]
        assert "Karisa"==data["data"]["othername"]
        assert "True"==data["data"]["isAdmin"]

    def test_register_user_empty_values(self,cli_ent):
        """
        This intance method tests if user values passed are empty
        """
        response=cli_ent.post('/api/v1/registration',
            data=json.dumps(dict(
                firstname="  ",secondname="  ",
                othername="Karisa",email="jumamasha@gmail.com",
                username="Juma",isAdmin="True",
                phonenumber="0727645367",password="1234",
                confirmpassword="1234"
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert "All user's information is required to register" in data["error_msg"]

    def test_register_user_invalid_values(self,cli_ent):
        """
        This instance method tests if the user values passed are valid
        """
        response=cli_ent.post('/api/v1/registration',
        data=json.dumps(dict(
                firstname=1234,secondname=1234,
                othername="Karisa",email="jumamasha@gmail.com",
                username="Juma",isAdmin="True",
                phonenumber="0727645367",password="1234",
                confirmpassword="1234"
            )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert "Please provide user valid values" in data["error_msg"]
        assert 400==data["status"]

    def test_register_user_invalid_email(self,cli_ent):
        response=cli_ent.post('/api/v1/registration',
            data=json.dumps(dict(
                firstname="Juma",secondname="Masha",
                othername="Karisa",email="jumamashagmail.com",
                username="Juma",isAdmin=True,
                phonenumber="0727645367",password="1234",
                confirmpassword="1234"
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert "Please provide a valid email" in data["error_msg"]
        assert 400==data["status"]

class TestLoginUser():
    
    def test_login_user(self,cli_ent):
        """
        This instance method test for successful sign in of users
        """ 
        response=cli_ent.post('/api/v1/login',
            data=json.dumps(dict(
                email="jumamasha@gmail.com",
                password="1234"
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==200
        assert data["data"]["email"]=="jumamasha@gmail.com"
        assert data["data"]["isAdmin"]=="True"
    
    def test_login_user_empty_values(self,cli_ent):
        """
        This instance method test when user passes empty credentials
        """ 
        response=cli_ent.post('/api/v1/login',
            data=json.dumps(dict(
                email=" ",
                password=" "
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert data["error_msg"]=="Please fill both email and password to login"
    
    def test_login_user_invalid_email(self,cli_ent):
        """
        This instance method test when user passes invalid email
        """ 
        response=cli_ent.post('/api/v1/login',
            data=json.dumps(dict(
                email="jumamashagmail.com",
                password="1234"
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert data["error_msg"]=="Please provide a valid email"
 
    def test_login_user_email_notfound(self,cli_ent):
        """
        This instance method test when the email doesn't
        """
        response=cli_ent.post('/api/v1/login',
            data=json.dumps(dict(
                email="yahyanyiro@gmail.com",
                password="1234"
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==401
        assert data["error_msg"]=="The user's email provided doesn't exist"
      
    def test_login_user_password_incorrect(self,cli_ent):
        """
        This instance method test when the password in incorrect
        """ 
        response=cli_ent.post('/api/v1/login',
            data=json.dumps(dict(
                email="jumamasha@gmail.com",
                password="4321"
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==401
        assert data["error_msg"]=="The user's password provided is incorrect"