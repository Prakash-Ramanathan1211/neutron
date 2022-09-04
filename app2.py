from flask import Flask
from flask import render_template, request,jsonify

import random
import json
import pymongo
from pymongo import MongoClient
# import json
from bson import json_util
from flask import Markup
value = Markup('First line.<br>Second line.<br>')

cluster = MongoClient('mongodb+srv://prakash-1211:prakash@cluster0.enw9p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["neutron"]
col = db["user_details"]

app = Flask(__name__)

@app.route("/")
def hello_world():

    return render_template("login.html")


@app.route("/submit", methods=["GET","POST"])
def submit():
    name = request.form.get("feature-title")
    desc  = request.form.get("short_summary")

    col.insert_one({ "Name": name , "description": desc })
    for x in col.find():
        
       

        val=x['Name']
        val2=x['description'] 
    result = {
        'Name' : val ,
        'description' : val2
    }  
    # {{ org.backgroundInfo | replace(‘\n’, ‘<br>’) }} 

    # return json.dumps(result) 
    return render_template('result.html', result = result)

@app.route('/signup', methods=['POST'])
def page_signup_post():    

    username    = request.values.get('username')

    password    = request.values.get('password')

    data = {
        "username" : username,
        "password" : password,
        "ismentor" : False
        
    }
    result_dict = col.insert_one(data)

    return "Successfully signed up"

# @app.route('/login', methods=['POST'])
# def page_login_post():   

#     username    = request.values.get('username')

#     password    = request.values.get('password')

@app.route('/model',methods=['GET'])
def model():
    return render_template('prakah.html')


@app.route('/leetcode',methods=['GET'])
def leetcode():
    return render_template('leetcode-difficulty.html')

@app.route('/codechef/ranking',methods=['GET'])
def codechef1():
    return render_template('codechef-ranking.html')

@app.route('/codechef/rating',methods=['GET'])
def codechef2():
    return render_template('codechef-rating.html')

@app.route('/codechef/solvecount',methods=['GET'])
def codechef3():
    return render_template('codechef-solvecount.html')

@app.route('/leetcode/difficulty',methods=['GET'])
def leetcode1():
    return render_template('leetcode-difficulty.html')

@app.route('/codeforces/rating',methods=['GET'])
def codeforces():
    return render_template('cf-rating.html')


@app.route('/api/codeforces',methods=['GET'])
def get_codeforces_data():
    with open("codeforces.json") as f:
        data = json.load(f)
    res=[]
    for d in data["contests"]:
        res.append([d["Contest"], int(d["New Rating"])])
    return jsonify(res)

@app.route('/api/hackerearth',methods=['GET'])
def get_hackerearth_data():
    with open("hackerearth.json") as f:
        data = json.load(f)
    res=[]
    for d in data["users"]:
        print(d)  
        print(d.keys()) 

        res.append([d.keys()])
    return jsonify(res)


if __name__ == "__main__":
   
    app.run(debug=True)