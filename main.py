from flask import Flask,request,render_template,redirect
import jinja2
import os
import cgi

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir), autoescape=True)

app=Flask(__name__)
app.config['DEBUG']=True

#@app.route('/')
#def index():
    #return 

username = " "
usr_pwd = " "
vfry_pwd = " "
email = " "

@app.route('/', methods=['POST','GET'])
def sign_up_form():
    template=jinja_env.get_template('user_name.html')
    return template.render(username=username)
    

app.run()