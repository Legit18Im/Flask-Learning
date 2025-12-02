from flask import Flask,render_template,request


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

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")  # This function renders the "index.html" template when the "/index" URL is accessed.
 
@app.route("/about")
def about():
    return render_template("about.html")  # This function renders the "about.html" template when the "/about" URL is accessed.


@app.route("/form", methods=["GET","POST"])
def form():
    if request.method == "POST":
        # Process the form data here
        name = request.form.get("name")
        return f"Hello, {name}! Your form has been submitted."
    return render_template("form.html")  # Render a form template for GET requests


if __name__ == "__main__":# this block ensures that the Flask application runs only when the script is executed directly, not when imported as a module.
    app.run(debug = True)  # This starts the Flask development server with debug mode enabled.