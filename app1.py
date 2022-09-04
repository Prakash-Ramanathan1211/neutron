from flask import Flask
from flask import render_template, request
import business1


app = Flask(__name__)

@app.route("/")
def hello_world():

    return render_template("index.html")

@app.route('/login', methods=['POST'])
def page_signup_post():    

    username    = request.values.get('username')
    print(username) 

    password1    = request.values.get('password')
    # print(password)
 
    # time.sleep(3)
    login_route = business1.login(username,password1)

    return "success"




if __name__ == "__main__":
   
    app.run(debug=True)