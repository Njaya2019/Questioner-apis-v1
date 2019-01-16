from werkzeug.security import check_password_hash,generate_password_hash

#A global list to store users
users_list=[]

class users_model():
    """
    A class that has instance variables and class methods
    """
    def __init__(self,first_name,last_name,email,username,isAdmin,phonenumber,password,confirm_pwd):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.username=username
        self.isAdmin=isAdmin
        self.phonenumber=phonenumber
        self.password=password
        self.confirm_pwd=confirm_pwd
        self.user_id=len(users_list)+1
    def register_user(self):
        """
        An instance method to add a user to user's list global
        """
        if self.password!=self.confirm_pwd:
            return "The passwords do not match"
        for user in users_list:
            if user['email']==self.email:
                return "The email already exists. Choose another email"
        hashed_password=generate_password_hash(self.password)
        users_dict={
            "id":self.user_id,'firstname':self.first_name,
            'lastname':self.last_name,'isAdmin':self.isAdmin,
            'email':self.email,"phonenumber":self.phonenumber,
            "username":self.username,'password':hashed_password
            }
        users_list.append(users_dict)
        return {
            "id":self.user_id,'firstname':self.first_name,
            'lastname':self.last_name,'isAdmin':self.isAdmin,
            'email':self.email,"username":self.username,
            "phonenumber":self.phonenumber
            }

    @classmethod
    def signin_user(cls,email,password):
        """
        A class method to sigin a user
        """
        for user in users_list:
            if user["email"]==email:
                stored_pwd=user["password"]
                if check_password_hash(stored_pwd,password):
                    return user
                else:
                    return "The user's password provided is incorrect"
        return "The user's email provided doesn't exist"