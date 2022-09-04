from flask import Flask
from flask import render_template, request,jsonify,redirect,url_for

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


def get_last_user_id():

    last_user_id      = col.find().sort([('user_id',-1)]).limit(1)
    
    try:
        last_user_id = last_user_id[0]['user_id']
    except:
        last_user_id = 0

    # user_id = last_user_id + 1

    return last_user_id


@app.route('/signup', methods=['GET'])
def page_signup_get():  

    return render_template("signup.html")  


@app.route('/signup', methods=['POST'])
def page_signup_post():    

    username    = request.values.get('username')

    password    = request.values.get('password')

    user_id = get_last_user_id()
    new_user_id = user_id + 1
    data = {

        "user_id"  : new_user_id,
        "username" : username,
        "password" : password,
        "ismentor" : False
        
    }
    result_dict = col.insert_one(data)

    return "Successfully signed up"

# @app.route('/error-page', methods=['GET'])
# def error_page():   

#     return render_template("error.html")

@app.route('/login', methods=['POST'])
def page_login_post():   

    username    = request.values.get('username')

    password    = request.values.get('password')

    user = col.find_one({"username":username})

    user_id = user["user_id"]  

    print("********************8",user["password"])

    if user["password"] == password:
        if user["ismentor"]:
            
            return redirect(f'/mentor/{user_id}')
            
        else:
            return redirect(f'/mentee/{user_id}')
    
    else:
        return render_template("error.html")

@app.route('/mentor/<user_id>', methods=['GET'])
def mentor_page(user_id):   

    return render_template("mentor.html")

@app.route('/mentee/<user_id>', methods=['GET'])
def mentee_page(user_id):   

    return render_template("mentee.html")

@app.route('/model',methods=['GET'])
def model():
    return render_template('prakah.html')


@app.route('/leetcode',methods=['GET'])
def leetcode():
    return render_template('leetcode-difficulty.html')

@app.route('/codechef/ranking',methods=['GET'])
def codechef1():
    return render_template('cc-ranking.html')

@app.route('/codechef/rating',methods=['GET'])
def codechef2():
    return render_template('cc-rating.html')

@app.route('/codechef/solvecount',methods=['GET'])
def codechef3():
    return render_template('cc-solvecount.html')

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