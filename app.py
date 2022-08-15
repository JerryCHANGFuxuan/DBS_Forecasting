#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 11:39:50 2022

@author: changfuxuan
"""

from flask import Flask, render_template, request
app = Flask(__name__)

import joblib

@app.route("/", methods= ["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model3 = joblib.load("regression DBS")
        r1 = model3.predict([[rates]])
        model4 = joblib.load("tree DBS")
        r2 = model4.predict([[rates]])
        return(render_template("index.html", result1 = r1, result2 = r2))
    else:
        return(render_template("index.html", result1 = "waiting", result2 = "waiting"))
    
if __name__ == "__main__":
    app.run(host = 'localhost', port = 5001, debug = False)