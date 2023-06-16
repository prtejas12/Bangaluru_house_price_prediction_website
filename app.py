from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)
model = pickle.load(open("price.pkl","rb"))

dataset=pd.read_csv("dataset.csv")

@app.route("/")
def index():
    location=sorted(dataset["location"].unique())
    return render_template("input.html",location=location)


@app.route("/predict", methods=["POST"])
def predict():
    location= request.form.get("area")
    bath = float(request.form.get("bath"))
    sqft = request.form.get("sqft")
    bedroom = request.form.get("bedrooms")
    print(location,sqft,bath,bedroom)
    imput=pd.DataFrame([[location,sqft,bath,bedroom]],columns=["location","total_sqft","bath","bedroom"])
    res = model.predict(imput)[0]
    return str(np.round((res*1e5),2));

if __name__ == "__main__":
    app.run(debug=True)
