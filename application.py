from flask import Flask, jsonify
from app.endpoints.meetups import meetups_blueprint
from app.endpoints.questions import questions_blueprint
from app.endpoints.users_auth import userauth_blueprint

def create_app():
    """
    Creates a flask app
    """
    app=Flask(__name__)
    """
    register flask blueprints
    """
    app.register_blueprint(meetups_blueprint)
    app.register_blueprint(questions_blueprint)
    app.register_blueprint(userauth_blueprint)
    return app

app=create_app()
@app.errorhandler(404)
def page_not_found(error):
    """
        This error hundler returns a json message when
         the resource requested wasn't found
    """
    return jsonify({
        "error":"The requested resource wasn't found",
        "status": 404
        }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """
        This error hundler returns a json message that
         the request couldn't be performed.
    """
    return jsonify({
        "error":"The request made cannot be performed",
        "status": 405
        }), 405

@app.errorhandler(403)
def forbidden(error):
    """
        This error hundler returns a json message that
         the request access has been denied because one
         doesn't have access rights.
    """
    return jsonify({
        "error":"The request has been denied. Get access rights first",
        "status": 403
        }), 403
@app.errorhandler(400)
def bad_request(error):
    """
        This error hundler returns a json message the
         request sent invalid and the user has to modify 
         it before resending.
    """
    return jsonify({
        "error":"There request is invalid, change the values and try again",
        "status": 400
        }), 400

@app.errorhandler(500)
def internal_erro(error):
    """
        This error hundler returns a json message that
         there is a programming error or the server is 
         overloaded.
    """
    return jsonify({
        "error":"There is a programming error or the server is overloaded",
        "status": 500
        }), 500
    


if __name__=="__main__":
    """
    Runs flask application
    """
    app.run(debug=True)