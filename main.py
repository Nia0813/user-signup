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


#@app.route('/', methods=['POST'])
#My helper functions that all fields use
#is the field blank or do it contain spaces?
def isnt_empty(info):
    if info != "":
        return True
    else:
        return False

def no_space(info):
    emptyspace= " "
    if emptyspace not in info:
        return True
    else:
        return False

def email_val(info):
    accept_email = re.compile("[a-zA-Z0-9_]+\.?[a-zA-Z0-9_]+@[a-z]+\.[a-z]+")
    if accept_email.match(info):
        return True
    else:
        return False


#def text_length(info): not sure if i want to put this one here as it need each field name??
#conditonals
@app.route('/', methods=['POST'])
def validation_reqs():
#link to form input variables
    username=request.form['username']
    user_pwd=request.form['user_pwd']
    vrfy_pwd=request.form['vrfy_pwd']
    email=request.form['email']

#empty strings for error messages
    error_username = ""
    error_user_pwd = ""
    error_vrfy_pwd = ""
    error_email = ""
    error_char_len=""
    error_char_len1=""
    error_char_len2=""
    error_symbol=""
    error_emptyspace=""
    

    
    if not isnt_empty(username):
        error_username = "Username can not be empty"

    else:
        username_len = len(username)
        if username_len < 3 or username_len > 20:
            error_char_len= "Username must contain between 3 and 20 characters"
            
        else:
            if not no_space(username): 
               error_emptyspace= "Username can not contain spaces"                                          
                

    if not isnt_empty(user_pwd):
        error_user_pwd= "Password can not be empty"
    else:
        user_pwd_len= len(user_pwd)
        if user_pwd_len < 3 or user_pwd_len > 20:
            error_char_len1= "Password must contain between 3 and 20 characters"
            
        else:
            if not no_space(user_pwd): 
                error_emptyspace="Password can not contain spaces"                

   
    if vrfy_pwd != user_pwd:
            error_vrfy_pwd= "Passwords do not match"
        
                

    
    
    email_len= len(email)
    # print(len(email))
    if email_len < 1:
        pass
    else:
        if email_len < 3 or email_len > 20:
            error_char_len2= "Email must contain between 3 and 20 characters"
        else:
            if not no_space(email): 
                error_emptyspace="Email can not contain spaces"
            else: 
                if email_val == False:
                    error_symbol = "Email must contain one @ and one ."
        


    if not error_username and not error_user_pwd and not error_vrfy_pwd and not error_email:
        return render_template("welcome_page.html", username=username)
    else:
        return render_template ("user_name.html", username= username, email=email,user_pwd=user_pwd, vrfy_pwd=vrfy_pwd,
        error_username=error_username, error_user_pwd=error_user_pwd, error_vrfy_pwd=error_vrfy_pwd, error_email=error_email,
        error_emptyspace=error_emptyspace, error_char_len=error_char_len,error_char_len1=error_char_len1,error_char_len2=error_char_len2,error_symbol=error_symbol)
        
app.route("/welcome")
def welcome():
    username=request.args.get("username")
    return render_template(welcome.html, username=username)


app.run()