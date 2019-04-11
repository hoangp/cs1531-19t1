from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        zID = int(request.form["zID"])
        desc = request.form["desc"]
        #return render_template("hello.html", name=name, id=zID, desc=desc)
        #return redirect(url_for('hello', name=name, id=zID, desc=desc))
        user_input['name'] = name
        user_input['zID'] = zID
        user_input['desc'] = desc
        return redirect(url_for('hello'))
    return render_template("index.html")

@app.route("/Hello")
def hello():
    
    #name = request.args.get('name')
    #zid = request.args.get('id')
    #desc = request.args.get('desc')

    name = user_input['name']
    zid = user_input['zID']
    desc = user_input['desc']

    return render_template("hello.html", name=name, id=zid, desc=desc)

