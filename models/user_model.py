from werkzeug.security import check_password_hash,generate_password_hash

#A global list to store users
users_list=[]

class users_model():
    """
    A class that has instance variables and class methods
    """
    def __init__(self,first_name,second_name,gender,email,account_type,password,confirm_pwd):
        self.first_name=first_name
        self.second_name=second_name
        self.gender=gender
        self.email=email
        self.account_type=account_type
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
        account=users_model.acconttype_to_boolean(self.account_type)
        hashed_password=generate_password_hash(self.password)
        users_dict={
            "user_id":self.user_id,'user_firstname':self.first_name,
            'user_secondname':self.second_name,'isAdmin':account,
            'user_gender':self.gender,'email':self.email,
            'password':hashed_password
            }
        users_list.append(users_dict)
        return {
            "user_id":self.user_id,'user_firstname':self.first_name,
            'user_secondname':self.second_name,'isAdmin':account,
            'user_gender':self.gender,'email':self.email,
            }
    @classmethod
    def acconttype_to_boolean(cls,accounttype):
        """
        A class method to convert user account type to boolean
        """
        if accounttype=='Admin':
            isAdmin=True
            return isAdmin
        else:
            return False
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