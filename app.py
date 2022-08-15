#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 11:39:50 2022

@author: changfuxuan
"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods= ["GET","POST"])
def index():
    if request.method == "post":
        return(render_template("index.html", result1 = "temp", result2 = "temp"))
    else:
        return(render_template("index.html", result1 = "waiting", result2 = "waiting"))
    
if __name__ == "__main__":
    app.run(host = 'localhost', port = 5001, debug = False)