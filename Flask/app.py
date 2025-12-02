from flask import Flask


'''
It createas a Flask application instance.
which is the main component of a Flask web application.
which will be your WSGI application.
'''
### WSGI application
#entry point of the application
app = Flask(__name__)  # The __name__ variable helps Flask determine the root path of the application.

@app.route("/")  # This decorator defines a route for the root URL ("/") of the web application.
def welcome():
    return "Welcome to Flask Application!!!!.This is our fisrt application"  # This function returns a simple welcome message when the root URL is accessed.

@app.route("/index")
def index():
    return "This is the index page of our Flask Application"  # This function returns a message for the "/index" URL.
 
 



if __name__ == "__main__":# this block ensures that the Flask application runs only when the script is executed directly, not when imported as a module.
    app.run(debug = True)  # This starts the Flask development server with debug mode enabled.