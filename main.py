# create a user sign up with username, password, verify password, and email
# error when leaving fields empty

from flask import Flask, render_template, request
import jinja2
import re

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST', 'GET'])
#@app.route('/index')




def index():

    #variable names and error messages
    #inputs can not be empty     
    username = ""
    email = ""
    password =""
    verify_password = ""
    error_username = ""
    error_password = ""
    error_password_verification = ""
    error_email_message = ""

    if request.method == 'POST':

        #request information
        username = request.form['username']

        if username == " ":
            error_username = "The username can not be blank."

        for i in username:

            if i.isspace():
                # or username.isspace? add character limit?
                error_username = "Spaces are not allowed in the username."


#########
            
            password = request.form['password']
            

            for i in password:
                
                if i.isspace():
                    error_password = "Passwords can not have spaces."

                

#####       
            verify_password = request.form['verify_password']
           
            
            #redundant because of password = verification password in prev step
            for i in verify_password:

                if i.isspace():
                    error_password = "Passwords may not contain spaces"

            if password != verify_password:
                error_password_verification = "The passwords do not match."
        
            email = request.form['email']
        #must contain @ and ., only one @?
        #make allowed character set?
        #what do most okay email logins have?
        #email address may be blank

            #if email.count('@') != 1:
                #error_email_message = "The email address must contain one @."
            
            for i in email:

                if i.isspace():
                    error_email_message = "The email address can not contain a space."
                


    #verify and validate information: no spaces, no invalid characters
    #passwords are the same

    #put in correct form to render
    if (not error_username) and (not error_password) and (not error_password_verification) and (not error_email_message):   
        return render_template('index.html', 
            username=username, password=password, email=email, 
            verify_password=verify_password, error_email_message=error_email_message, error_password=error_password, error_username=error_username,error_password_verification=error_password_verification)
    
    
    return render_template('hello_user.html', username=username)
    


### main

app.run()
