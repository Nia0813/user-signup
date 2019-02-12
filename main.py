from flask import Flask,request,render_template,redirect
import jinja2
import os
import cgi

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir), autoescape=True)

app=Flask(__name__)
app.config['DEBUG']=True


#make form show
@app.route('/', methods=['GET'])
def sign_up_form():
    template=jinja_env.get_template('user_name.html')
    return template.render()
#conditionals
@app.route('/', methods=['POST'])
#helper functions

def validation_reqs():
    if len(username >= 3 or username <= 20):
        return (False)
    elif user_pwd == vrfy_pwd:
        return (False)
    else: 
        if len(email < 0):
            return (False)
        elif char >= 3 or char <= 20:
            return (False)
        elif email != " ":
            return (False)
        #elif "@" == 1 and "." == 1        
        else:
            return (True)
    
    


        


@app.route("/welcome")
def welcome():
    username=request.args.get("username")
    return render_template(welcome.html, username=username)


#@app.route('/user_pwd', methods=['POST'])
#error messages
def error_messages():
    error_username= "Please enter a valid username"
    error_user_pwd= "Please enter a valid password"
    error_vrfy_pwd= "Passwords do not match"
    error_email= "Please enter a valid email"

#Conditionals


#if user type nothing at all username
def index():
    if (password==" "):
       error="please enter password"
       return error
#link to form input variables
#username=request.form('username')
#user_pwd=request.form('user_pwd')
#vrfy_pwd=request.form('vrfy_pwd')
#email=request.form('email')

#empty strings for error messages
#username = " "
#user_pwd = " "
#vrfy_pwd = " "
#email = " "    

app.run()