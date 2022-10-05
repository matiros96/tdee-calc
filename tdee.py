# https://github.com/alanbanks229/flask_calculator_app
from flask import Flask, redirect, render_template, request, url_for
from processing import do_calculation

__author__ = "Soren Matiros"
__version__ = "0.1.0"
__license__ = "MIT"


app = Flask(__name__)
app.config["DEBUG"] = True

#decalation of values
bmr = 0
weight = 0
height = 0
age = 0
gender = 'male'
activity = 0

@app.route("/", methods=["GET"])
def index():
    """Render index"""
    return render_template("main.html")

@app.route('/operation_result/', methods=['POST'])
def operation_result():
    """Route where we send calculator form input"""
    error = None
    bmr_result = None
    tdee_result = None
    
    # request.form looks for:
    # html tags with matching "name= "
    weight = request.form['weight'] 
    height = request.form['height']
    age = request.form['age']
    algo = request.form['algo']
    gender = request.form['gender']
    activity = request.form['activity']
    try:
        weight = float(weight)
        height = float(height)
        age = float(age)
        activity = float(activity)

        # On default, the operation on webpage is addition
        if algo == "jeor":
            bmr_result = do_calculation(weight, height, age, gender, algo)
            tdee_result = bmr_result * activity
        elif operation == "-":
            bmr_result = input1 - input2

        return render_template(
            'main.html',
            algo=algo,
            bmr_result=bmr_result,
            tdee_result=tdee_result,
            calculation_success=True
        )
        
    except ZeroDivisionError:
        return render_template(
            'main.html',
            #input1=input1,
            #input2=input2,
            algo=algo,
            bmr_result="Bad Input",
            calculation_success=False,
            error="You cannot divide by zero"
        )
        
    except ValueError:
        return render_template(
            'main.html',
            #input1=first_input,
            #input2=second_input,
            algo=algo,
            bmr_result="Bad Input",
            calculation_success=False,
            error="Try again."
        )