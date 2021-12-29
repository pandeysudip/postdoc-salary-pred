from flask import Flask, render_template, redirect, jsonify, request
import json
from bson import json_util
import utilis
# Create an instance of Flask
app = Flask(__name__)


@app.route('/')
def home():
    # Return the template
    return render_template('index.html')


@app.route('/index.html', methods=["GET", "POST"])
def predic():

    if request.method == "POST":
        Rating = request.form.get('Rating')
        Size = request.form.get("Size")
        Typeofownership = request.form.get("Type of ownership")
        Industry = request.form.get('Industry')
        Sector = request.form.get('Sector')
        Revenue = request.form.get('Revenue')
        State = request.form.get(
            'State')
        desc_length = request.form.get('desc_length')
        variables = [Rating, Size, Typeofownership,  Industry,
                     Sector, Revenue, State, desc_length]
        predict = utilis.preprocess(variables)
        predict, *_ = predict
        # Return the template
        return render_template("index.html", pred=variables, prediction=predict)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
