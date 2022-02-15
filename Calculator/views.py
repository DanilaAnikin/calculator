"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from Calculator import app
from Calculator.Backend import Solver

solver = Solver()

@app.route('/')
@app.route('/calculator')
def calculator():
    """Renders the home page."""
    return render_template(
        'calculator.html'
    )

@app.route('/about_me')
def about_me():
    """Renders the home page."""
    return render_template(
        'about_me.html'
    )

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/calculate',methods=["GET", "POST"])
def calculate():
    print("request.args: " + str(request.args))
    result = solver.solve(request.args.get("input"))
    print("result: " + str(result))
    return str(result)
